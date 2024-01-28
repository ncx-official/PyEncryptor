from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from getpass import getpass
import binascii
import os

def encrypt_text_with_aes(password, plaintext):
    # Derive a key from the password using PBKDF2
    salt = b'salt_1234'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=salt,
        iterations=100000,
        length=32
    )
    key = kdf.derive(password.encode())

    # Generate a random IV (Initialization Vector)
    iv = os.urandom(16)

    # Encrypt the plaintext using AES in CFB mode
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()

    # Convert the bytes of the encrypted text to a hexadecimal string
    encrypted_text_hex = binascii.hexlify(iv + ciphertext).decode()

    return encrypted_text_hex

def main():
    password = getpass("Enter your password: ")
    plaintext = input("Enter the text to encrypt: ")
    encrypted_text = encrypt_text_with_aes(password, plaintext)

    print("\nPassword: {}".format(password))
    print("Original Text: {}".format(plaintext))
    print("Encrypted Text: {}".format(encrypted_text))

if __name__ == "__main__":
    main()
