#!/usr/bin/env python3
# AES files cryptor
# By Nasikovskyi Vitalii
# started 2-1-2024
# finished ...

# import tkinter as tk
# from tkinter import filedialog
from encrypt_data import encrypt_text, encrypt_file
from decrypt_data import decrypt_text, decrypt_file

# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.title("File/Text Encrypter")
#         self.geometry("400x200")

#         self.init_ui()

#     def init_ui(self):
#         # Create widgets
#         self.label = tk.Label(self, text="Enter text:")
#         self.text_entry = tk.Entry(self, width=30)
#         self.encrypt_button = tk.Button(self, text="Encrypt", command=self.encrypt_text)
#         self.decrypt_button = tk.Button(self, text="Decrypt", command=self.decrypt_text)

#         # Grid layout
#         self.label.grid(row=0, column=0, padx=10, pady=10)
#         self.text_entry.grid(row=0, column=1, padx=10, pady=10)
#         self.encrypt_button.grid(row=1, column=0, columnspan=2, pady=10)
#         self.decrypt_button.grid(row=2, column=0, columnspan=2, pady=10)

#     def encrypt_text(self):
#         text_to_encrypt = self.text_entry.get()
#         encrypted_text = encrypt_text(text_to_encrypt)
#         tk.messagebox.showinfo("Encrypted Text", f"Encrypted Text: {encrypted_text}")

#     def decrypt_text(self):
#         text_to_decrypt = self.text_entry.get()
#         decrypted_text = decrypt_text(text_to_decrypt)
#         tk.messagebox.showinfo("Decrypted Text", f"Decrypted Text: {decrypted_text}")

# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

password = "123452"
text = "Hello world3!"

enc_text = encrypt_text(text=text, password=password)
print(enc_text)

dec_text = decrypt_text(encrypted_text=enc_text, password=password)
print(dec_text)