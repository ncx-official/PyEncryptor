from PySide6.QtCore import QObject
from crypto_service_utility import CryptoServiceUtility

class AppController(QObject):
    
    def __init__(self):
        super().__init__()

    def textEncryptor(self, text, password):
        # Validate inputs
        if not self.validate_text(text) or not self.validate_password(password):
            return None, False
        
        try:
            result_text = CryptoServiceUtility.encrypt_text(text=text, password=password)
            status = True
        except Exception as e:
            print(f"Encryption error: {e}")
            result_text = None
            status = False

        return result_text, status

    def textDecryptor(self, text, password):
        # Validate inputs
        if not self.validate_text(text) or not self.validate_password(password):
            return None, False
        
        try:
            result_text = CryptoServiceUtility.decrypt_text(text=text, password=password)
            status = True
        except Exception as e:
            print(f"Decryption error: {e}")
            result_text = None
            status = False

        return result_text, status

    def validate_text(self, text):
        if 0 < len(text) <= 100000:
            return True
        else:
            print("Text must be 1 to 100000 characters long.")
            return False

    def validate_password(self, password):
        if 6 <= len(password) <= 25:
            return True
        else:
            print("Password must be 6 to 25 characters long.")
            return False

    def fileEncryptor():
        pass

    def fileDecryptor():
        pass

"""
   def sendTextEcnryptor(self):
        user_input = self.InputEncryptionTextBox.toPlainText()
        password = self.InputEncryptionPasswordLine.text()
        encrypted_text, status = self.controller.textEcnryptor(user_input, password)       
        self.OutputEncryptionTextBox.setText(encrypted_text)
        #TODO: if status - success -> create "Success" lable, else -> "Failure"

    def sendTextDecryptor(self):
        user_input = self.InputDecryptionTextBox.toPlainText()
        password = self.InputDecryptionPasswordLine.text()
        decrypted_text, status = self.controller.textDecryptor(user_input, password)  
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
"""

    #TODO: def encryptText(self):
    # Try Except for user input
    # + Try Except for encryption proccess
    # + Checking for incorrect password
    # + Check if Input Text is not zero
    # + Add success label text if encryption/decryption failed or succeed
    

    #TODO: def decryptText(self):
    # Try Except for user input 
    # + Try Except for decryption proccess
    # + Checking for incorrect password
    # + Add success label text if encryption/decryption failed or succeed
    

    #TODO: # def actionFile(self):
    # Try Except for user input 
    # + Try Except for encryption proccess
    # + implement checking method if file with "UserInputName" possible to create, if not -> create random with ".encr" name
    # + Checking for incorrect password
    # + Is file selected, if not -> send pop-up to choose the file
    # + Save processed files in the same path as original provided
    # + Change logs button name, change "new file name" button object name
    # + Add success label text if encryption/decryption failed or succeed
    # if filePath:  # Proceed only if a file is selected
    


# TODO: Enforce Password Complexity
# Implement user input password checking for encrypting data. Allow only strong password.


# TODO: Set min and max password length for encr/decr and check what if password would be more that 256-bit
    
# TODO: Implement "show password" checkbox
    
#  Implement Global TRY EXCEPT for every piece of code
    
#  Set max input values for textboxes




### MAYBE LATER PART
# Add feature to choose password length (128-bit, 192-bit, 256-bit)

# Add feature to choose custom salt size 

# separate thread or using asynchronous programming patterns
#  This prevents the UI from freezing while the operation is in progress. PyQt/PySide has the QThread class, and Python has the threading module, which can be used for such purposes.
    
# Think about to make files encrypt_data.py and decrypt_data.py as separate classes (not just functions)