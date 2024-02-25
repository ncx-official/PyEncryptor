from PySide6.QtWidgets import QMainWindow, QFileDialog, QRadioButton
from ui_main_window import Ui_MainWindow
from app_controller import AppController

class UserInterface(QMainWindow, Ui_MainWindow):
    def __init__(self, controller: AppController):
        super().__init__()
        self.controller = controller
        self.setupUi(self)

        # UI Buttons
        self.pushTextButton.clicked.connect(self.displayTextStackedWidget)
        self.pushFileButton.clicked.connect(self.displayFileStackedWidget)
        self.pushContainerButton.clicked.connect(self.displayContainerStackedWidget)
        self.pushOpenFileButton.clicked.connect(self.displayFileDialogWidget)
        self.radioEncryptionButton.clicked.connect(self.onRadioFileButtonClicked)
        self.radioDecryptionButton.clicked.connect(self.onRadioFileButtonClicked)
        self.radioEncryptionButton.click()

        # Business Buttons
        self.EncryptTextButton.clicked.connect(self.sendTextEcnryptor)
        self.DecryptTextButton.clicked.connect(self.sendTextDecryptor)
        self.pushFileActionButton.clicked.connect(self.sendFileCryptor)

    def displayTextStackedWidget(self): # select "Text" stack tab
        # Find the index of self.TextStackedWidget in self.stackedWidget
        index = self.stackedWidget.indexOf(self.TextStackedWidget)
        self.stackedWidget.setCurrentIndex(index)

    def displayFileStackedWidget(self): # select "File" stack tab
        # Find the index of self.FileStackedWidget in self.stackedWidget
        index = self.stackedWidget.indexOf(self.FileStackedWidget)
        self.stackedWidget.setCurrentIndex(index)

    def displayContainerStackedWidget(self): # select "Containers" stack tab
        # Find the index of self.ContainerStackedWidget in self.stackedWidget
        index = self.stackedWidget.indexOf(self.ContainerStackedWidget)
        self.stackedWidget.setCurrentIndex(index)
    
    def displayFileDialogWidget(self): # Select "File" to encrypt/decrypt
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
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

    def sendTextEcnryptor(self):
        user_input = self.InputEncryptionTextBox.toPlainText()
        password = self.InputEncryptionPasswordLine.text()
        encrypted_text, status = self.controller.textEncryptor(text=user_input, password=password)       
        self.OutputEncryptionTextBox.setText(encrypted_text)
        #TODO: if status - success -> create "Success" lable, else -> "Failure"

    def sendTextDecryptor(self):
        user_input = self.InputDecryptionTextBox.toPlainText()
        password = self.InputDecryptionPasswordLine.text()
        decrypted_text, status = self.controller.textDecryptor(text=user_input, password=password)  
        self.OutputDecryptionTextBox.setText(decrypted_text)
        #TODO: if status - success -> create "Success" lable, else -> "Failure"

    def sendFileCryptor(self):
        file_path = self.lineFilePath.text()
        password = self.lineFilePassword.text()
        new_file_name = self.lineNewFileName.text()

        if self.radioEncryptionButton.isChecked():
            status = self.controller.fileEncryptor(file_path, password, new_file_name)
        else:
            status = self.controller.fileDecryptor(file_path, password, new_file_name)
        #TODO: if status - success -> create "Success" lable, else -> "Failure"
        #TODO: Add random function for progress bar values, if failure -> make it red and 0%