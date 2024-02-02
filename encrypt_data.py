import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def generate_key(password): # Generation 32-byte encryption key from provided user password
    salt = os.urandom(16) # Generate a random 16-byte (128-bit) salt
    kdf = PBKDF2HMAC( 
        algorithm=hashes.SHA256(),
        length=32, # Derive a 32-byte (256-bit) key
        salt=salt,
        iterations=480000, # Number of iterations for the PBKDF2 algorithm
    ) # key derivation function (KDF) 
    key = base64.urlsafe_b64encode(kdf.derive(password.encode())) 
    return key, salt

def encrypt_text(text, password): # Text encryption, symmetric key encryption (AES in CBC mode)
    key, salt = generate_key(password)
    cipher_suite = Fernet(key)
    encrypted_text = cipher_suite.encrypt(text.encode()) # convert string to bytes then encrypt
    return salt.hex() + encrypted_text.hex() # 16-byte salt and encrypted text into hex (just for good human readability)

def encrypt_file(file_path, password):
    with open(file_path, 'rb') as file:
        file_data = file.read() # get bytes

    key, salt = generate_key(password)
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(file_data) # encrypt bytes

    with open(file_path + ".enc", 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data + salt) # Add salt to encrypted file for use in decryption (last 16-byte)