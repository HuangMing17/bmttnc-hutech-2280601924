import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.ceasar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
    
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {  # Sửa lỗi tên biến
            "plain_text": self.ui.txt_plain.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher.setPlainText(data['encrypted_message'])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted successfully")
                msg.exec_()
            else:
                print("ERROR while calling API")  # Sửa lỗi chính tả
        except requests.exceptions.RequestException as e:
            print("Error: %s" % str(e))  # Sửa lỗi e.message
        
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {  # Sửa lỗi tên biến
            "cipher_text": self.ui.txt_cipher.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain.setPlainText(data['decrypted_message'])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted successfully")
                msg.exec_()
            else:
                print("ERROR while calling API")  # Sửa lỗi chính tả
        except requests.exceptions.RequestException as e:
            print("Error: %s" % str(e))  # Sửa lỗi e.message

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
