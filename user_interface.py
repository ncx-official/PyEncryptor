from PySide6.QtCore import Qt
from PySide6.QtGui import (QTextOption, QFont)
from PySide6.QtWidgets import (QDialog, QFileDialog, QLabel, QMainWindow, 
                               QRadioButton, QTextEdit, QVBoxLayout, QMessageBox, QLineEdit)
from ui_main_window import Ui_MainWindow
from app_controller import AppController
import random

class UserInterface(QMainWindow, Ui_MainWindow):
    def __init__(self, controller: AppController):
        super().__init__()
        self.controller = controller
        self.setupUi(self)
    
        # UI Buttons
        self.pushTextButton.clicked.connect(self.displayTextStackedWidget)
        self.pushFileButton.clicked.connect(self.displayFileStackedWidget)
        self.pushOpenFileButton.clicked.connect(self.displayFileDialogWidget)
        self.radioEncryptionButton.clicked.connect(self.onRadioFileButtonClicked)
        self.radioDecryptionButton.clicked.connect(self.onRadioFileButtonClicked)  
        self.pushAboutButton.clicked.connect(self.showAboutPopUp)
        self.radioEncryptionButton.click()
        self.TextTabWidget.currentChanged.connect(self.clearTextEncryptionFields)
        
        # Show password checkboxes
        self.checkFilePasswordBox.stateChanged.connect(self.toggleFilePasswordVisibility)
        self.checkTextPasswordEncrBox.stateChanged.connect(self.toggleTextEncryptPasswordVisibility)
        self.checkTextPasswordDecrBox.stateChanged.connect(self.toggleTextDecryptPasswordVisibility)
        self.InputEncryptionPasswordLine.setEchoMode(QLineEdit.Password)
        self.InputDecryptionPasswordLine.setEchoMode(QLineEdit.Password)
        self.lineFilePassword.setEchoMode(QLineEdit.Password)

        # Business Buttons
        self.EncryptTextButton.clicked.connect(self.sendTextEcnryptor)
        self.DecryptTextButton.clicked.connect(self.sendTextDecryptor)
        self.pushFileActionButton.clicked.connect(self.sendFileCryptor)
        self.controller.errorOccurred.connect(self.showErrorPopup)

    def displayTextStackedWidget(self): # select "Text" stack tab
        # Find the index of self.TextStackedWidget in self.stackedWidget
        index = self.stackedWidget.indexOf(self.TextStackedWidget)
        self.stackedWidget.setCurrentIndex(index)

    def displayFileStackedWidget(self): # select "File" stack tab
        # Find the index of self.FileStackedWidget in self.stackedWidget
        index = self.stackedWidget.indexOf(self.FileStackedWidget)
        self.stackedWidget.setCurrentIndex(index)

        
    def displayFileDialogWidget(self): # Select "File" to encrypt/decrypt
        options = QFileDialog.Options()
        # For a single file
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.lineFilePath.setText(fileName)

    def onRadioFileButtonClicked(self): # Select action method ("Encryption"/"Decryption")
        # Determine which button was clicked
        button = self.sender()
        
        if button is None or not isinstance(button, QRadioButton):
            return
        
        if button.isChecked():
            if button == self.radioEncryptionButton: # Encryption radio button is clicked
                self.pushFileActionButton.setText("Encryption")

            elif button == self.radioDecryptionButton: # Decryption radio button is clicked
                self.pushFileActionButton.setText("Decryption")

    def toggleFilePasswordVisibility(self):
        if self.checkFilePasswordBox.isChecked():
            self.lineFilePassword.setEchoMode(QLineEdit.Normal)
        else:
            self.lineFilePassword.setEchoMode(QLineEdit.Password)

    def toggleTextEncryptPasswordVisibility(self):
        if self.checkTextPasswordEncrBox.isChecked():
            self.InputEncryptionPasswordLine.setEchoMode(QLineEdit.Normal)
        else:
            self.InputEncryptionPasswordLine.setEchoMode(QLineEdit.Password)

    def toggleTextDecryptPasswordVisibility(self):
        if self.checkTextPasswordDecrBox.isChecked():
            self.InputDecryptionPasswordLine.setEchoMode(QLineEdit.Normal)
        else:
            self.InputDecryptionPasswordLine.setEchoMode(QLineEdit.Password)

    def sendTextEcnryptor(self):
        user_input = self.InputEncryptionTextBox.toPlainText()
        password = self.InputEncryptionPasswordLine.text()
        encrypted_text = self.controller.textEncryptor(text=user_input, password=password)       
        self.OutputEncryptionTextBox.setText(encrypted_text)

    def sendTextDecryptor(self):
        user_input = self.InputDecryptionTextBox.toPlainText()
        password = self.InputDecryptionPasswordLine.text()
        decrypted_text = self.controller.textDecryptor(text=user_input, password=password)  
        self.OutputDecryptionTextBox.setText(decrypted_text)

    def sendFileCryptor(self):
        self.progressFileBar.setValue(random.randint(10,38))  # Show that the process has started
        file_path = self.lineFilePath.text()
        password = self.lineFilePassword.text()
        new_file_name = self.lineNewFileName.text()

        if self.radioEncryptionButton.isChecked():
            status = self.controller.fileEncryptor(file_path, password, new_file_name)
        else:
            status = self.controller.fileDecryptor(file_path, password, new_file_name)

        if status:
            self.progressFileBar.setValue(100)  # Set progress bar to 100% on success      
            infoDialog = QMessageBox(self)
            infoDialog.setIcon(QMessageBox.Information)
            infoDialog.setWindowTitle("Success")
            infoDialog.setText(f"<font color='black'>The process completed successfully.</font>")
            infoDialog.setStandardButtons(QMessageBox.Ok)
            infoDialog.exec()  # Display the dialog
        
        self.lineFilePassword.clear()
        self.lineFilePath.clear()
        self.lineNewFileName.clear()
        self.progressFileBar.setValue(0)

        
    def showAboutPopUp(self):
        dialog = AboutDialog(self)
        dialog.exec()

    def showErrorPopup(self, message):
            # Create a QMessageBox instance with 'self' as its parent
            errorDialog = QMessageBox(self)
            errorDialog.setIcon(QMessageBox.Critical)
            errorDialog.setWindowTitle("Error")
            errorDialog.setText(f"<font color='black'>{message}</font>")
            errorDialog.setStandardButtons(QMessageBox.Ok)
            errorDialog.exec()  # Display the dialog
    
    def clearTextEncryptionFields(self):
        self.InputEncryptionTextBox.clear()
        self.InputDecryptionTextBox.clear()
        self.InputEncryptionPasswordLine.clear()
        self.InputDecryptionPasswordLine.clear()

        self.OutputDecryptionTextBox.clear()
        self.OutputEncryptionTextBox.clear()

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # Set QDialog size and title
        self.setWindowTitle("About")
        self.setObjectName(u"AboutDialogWindow")

        self.setFixedSize(285, 285)  # This sets both min and max sizes

        self.textEdit = QTextEdit(self)
        self.textEdit.setReadOnly(True)
        font = QFont("Courier", 10)
        self.textEdit.setFont(font)
        self.textEdit.setWordWrapMode(QTextOption.NoWrap)
        self.textEdit.setAlignment(Qt.AlignCenter)  # Center align text in QTextEdit
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # Hide the vertical scrollbar
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) # Hide the horizontal scrollbar
        self.textEdit.setObjectName(u"AboutDialogText")
        # Set the text
        self.textEdit.setText("█▀▀▀▀▀█ ▄█ ▀ ▀▄▄█ █▀▀▀▀▀█\n"
                              "█ ███ █ ▄▀█▄█▄▀ ▀ █ ███ █\n"
                              "█ ▀▀▀ █ ▄▄▄▀ █▄▄█ █ ▀▀▀ █\n"
                              "▀▀▀▀▀▀▀ ▀▄▀▄█ █ ▀ ▀▀▀▀▀▀▀\n"
                              "█▀█▀█▄▀██▀ ▄▀█▀▀▄▀ █ ▀ █\n"
                              " █▀▀ ▀▀▄█ ▀ ▄▀▀▀▄▄▄█▀▀ ▀█\n"
                              "▄▄  ▄▀▀█▄█▀█▀▀▀  █▀▄▀▄▀█▀\n"
                              "█ ▀ ▀▀▀█▄▄█▄▀▀▄▀ ▀███▀ ▀█\n"
                              "▀ ▀▀▀▀▀▀▄██▄▀████▀▀▀█▄▀\n"
                              "█▀▀▀▀▀█ ▀▀█▄▀   █ ▀ █▄▀█▀\n"
                              "█ ███ █ █▄█▄▀█ ▀▀██▀█▄██▄\n"
                              "█ ▀▀▀ █ █▄█▄  █ ▄  ▄▄█▀ █\n"
                              "▀▀▀▀▀▀▀ ▀  ▀▀▀▀   ▀▀▀▀▀▀▀")

        # Label with bold text
        self.licenseLabel = QLabel("MIT License © 2024 Nasikovskyi Vitalii")
        self.licenseLabel.setObjectName(u"AboutDialogLabel")
        self.licenseLabel.setAlignment(Qt.AlignCenter)  # Center alignment
        font = self.licenseLabel.font()  # Get the current font
        font.setBold(True)  # Make font bold
        self.licenseLabel.setFont(font)  # Set the bold font back

        # Layout to hold the QTextEdit and QLabel
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.licenseLabel)
        self.setLayout(layout)