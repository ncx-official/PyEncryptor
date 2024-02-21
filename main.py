#!/usr/bin/env python3
# AES files cryptor
# By Nasikovskyi Vitalii
# 2-1-2024

from encrypt_data import encrypt_text, encrypt_file
from decrypt_data import decrypt_text, decrypt_file
import sys

from PySide6 import QtWidgets
from user_interface import Ui_MainWindow


class UserInterface(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def App():
    app = QtWidgets.QApplication(sys.argv)
    window = UserInterface()
    
    window.show()
    app.exec()

if __name__ == "__main__":
    App()