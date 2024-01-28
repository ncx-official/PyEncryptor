from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import binascii
import base64
from getpass import getpass
import os

def encrypt_text_with_aes(password, plaintext):
    salt = b'salt_1234'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=salt,
        iterations=100000,
        length=32
    )
    key = kdf.derive(password.encode())
    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()

    encrypted_text_hex = binascii.hexlify(iv + ciphertext).decode()

    return encrypted_text_hex

def decrypt_text_with_aes(password, encrypted_text_hex):
    # Convert the hexadecimal string back to bytes
    encrypted_text_bytes = binascii.unhexlify(encrypted_text_hex)

    # Extract the IV and ciphertext from the encrypted text
    iv = encrypted_text_bytes[:16]
    ciphertext = encrypted_text_bytes[16:]

    # Derive the key from the password using PBKDF2
    salt = b'salt_1234'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=salt,
        iterations=100000,
        length=32
    )
    key = kdf.derive(password.encode())

    # Decrypt the ciphertext using AES in CFB mode
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()

    return decrypted_text.decode()

def main():
    password = getpass("Enter your password: ")
    plaintext = input("Enter the text to encrypt: ")
    encrypted_text = encrypt_text_with_aes(password, plaintext)

    print("\nPassword: {}".format(password))
    print("Original Text: {}".format(plaintext))
    print("Encrypted Text: {}".format(encrypted_text))

    decrypted_text = decrypt_text_with_aes(password, encrypted_text)
    print("Decrypted Text: {}".format(decrypted_text))

if __name__ == "__main__":
    main()
