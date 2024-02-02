import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def recreate_key(password, salt):
    kdf = PBKDF2HMAC( 
        algorithm=hashes.SHA256(),
        length=32, # Derive a 32-byte (256-bit) key
        salt=salt,
        iterations=480000, # Number of iterations for the PBKDF2 algorithm
    ) # key derivation function (KDF) 
    key = base64.urlsafe_b64encode(kdf.derive(password.encode())) 
    return key

def decrypt_text(encrypted_text, password):
    encrypted_text = bytes.fromhex(encrypted_text)  # Convert from hex to bytes
    salt = encrypted_text[:16] # Extract salt from the beginning 16-bytes 
    key = recreate_key(password, salt)
    cipher_suite = Fernet(key)
    decrypted_text = cipher_suite.decrypt(encrypted_text[16:]).decode() # Skip the first 16-bytes (salt)
    return decrypted_text

def decrypt_file(encrypted_file_path, password):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    salt = encrypted_data[-16:] # Extract salt from the ending
    key = recreate_key(password, salt)
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data[:-16]) # Skip the last 16 bytes (salt)

    original_file_path = encrypted_file_path[:-4]  # Remove '.enc' extension
    with open(original_file_path, 'wb') as original_file:
        original_file.write(decrypted_data)