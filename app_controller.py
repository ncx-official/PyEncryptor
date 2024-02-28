import os
from PySide6.QtCore import QObject, Signal
from crypto_service_utility import CryptoServiceUtility

class AppController(QObject):
    errorOccurred = Signal(str) # Make sure error signal is defined

    def __init__(self):
        super().__init__()

    def _validate_file_paths(self, open_path, new_file_name):
        # Check if open_path and new_file_name are valid
        if not open_path or not new_file_name:
            self.errorOccurred.emit("Open path or new file name is empty")
            return None

        # Validate new_file_name for illegal characters and ensure it is not a path
        if any(char in new_file_name for char in '\\/:*?"<>|') or os.path.basename(new_file_name) != new_file_name:
            self.errorOccurred.emit("New file name is invalid or unsafe")
            return None

        # Construct save_path from open_path directory and new_file_name
        save_path = os.path.join(os.path.dirname(open_path), new_file_name)

        # Check if the new file already exists
        if os.path.exists(save_path):
            self.errorOccurred.emit(f"A file with the name '{new_file_name}' already exists.")
            return None

        return save_path
    
    def textEncryptor(self, text, password):      
        try:
            result_text = CryptoServiceUtility.encrypt_text(text=text, password=password)
        except Exception as e:
            self.errorOccurred.emit(f"Encryption error: {str(e)}")
            result_text = None

        return result_text

    def textDecryptor(self, text, password):  
        try:
            result_text = CryptoServiceUtility.decrypt_text(text=text, password=password)
        except Exception as e:
            self.errorOccurred.emit(f"Decryption error: {str(e)}")
            result_text = None

        return result_text

    def fileEncryptor(self, open_path, password, new_file_name):
        save_path = self._validate_file_paths(open_path, new_file_name)
        if save_path is None:  # Validation failed
            return False

        # Proceed with encryption
        try:
            CryptoServiceUtility.encrypt_file(open_path, password, save_path)
            return True
        except Exception as e:
            self.errorOccurred.emit(f"File encryption error: {str(e)}")
            return False

    def fileDecryptor(self, open_path, password, new_file_name):
        save_path = self._validate_file_paths(open_path, new_file_name)
        if save_path is None:  # Validation failed
            return False

        # Proceed with decryption
        try:
            CryptoServiceUtility.decrypt_file(open_path, password, save_path)
            return True
        except Exception as e:
            self.errorOccurred.emit(f"File decryption error: {str(e)}")
            return False