#!/usr/bin/env python3
# AES files cryptor
# By Nasikovskyi Vitalii
# 2-1-2024

import sys
from PySide6.QtWidgets import QApplication
from app_controller import AppController
from user_interface import UserInterface

def main():
    app = QApplication(sys.argv)
    controller = AppController()
    mainWindow = UserInterface(controller)
    mainWindow.show()
    app.exec()

if __name__ == "__main__":
    main()