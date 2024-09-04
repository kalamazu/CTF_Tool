from PyQt5.QtWidgets import QTextEdit, QPushButton,QLabel
from PyQt5.QtWidgets import QTextBrowser
import Ui_untitled
import binascii

class MainWindow(Ui_untitled.Ui_MainWindow):
    def __init__(self,ui):
        super().__init__()
        self.ui = ui  
        self.setup_connections()
        self.current_page = self.ui.stackedWidget.currentWidget()
        self.browser=self.current_page.findChild(QTextBrowser, "textBrowser")
        self.data=self.current_page.findChild(QTextEdit, "data")

    def setup_connections(self):
        self.current_page = self.ui.stackedWidget.currentWidget()
        if self.current_page:
            hex_string_button = self.current_page.findChild(QPushButton, "pbhexstring")
            bigend_button = self.current_page.findChild(QPushButton, "pbbigend")
            xor_button = self.current_page.findChild(QPushButton, "pbxor")
            format_button = self.current_page.findChild(QPushButton, "pbformat")
            if hex_string_button:
                hex_string_button.clicked.connect(lambda:self.convert_to_string())
            else:
                print("Button 'pbhexstring' not found!")
            if bigend_button:
                bigend_button.clicked.connect(lambda:self.convert_to_bigend())
            else:
                print("Button 'pbbigend' not found!")
            if xor_button:
                xor_button.clicked.connect(lambda:self.xor_operation())
            else:
                print("Button 'pbxor' not found!")
            if format_button:
                format_button.clicked.connect(lambda:self.format_string())
            else:
                print("Button 'pbformat' not found!")
        else:
            print("Current page is not found!")

    def convert_to_string(self):
        string=bytes.fromhex(self.data.toPlainText()).decode('utf-8')
        self.browser.setText(string)

    def convert_to_bigend(self):
        string=bytes.fromhex(self.data.toPlainText()).decode('utf-8')
        self.browser.setText(binascii.hexlify(binascii.unhexlify(string)[::-1]))#[::-1]是将字符串反转，unhexlify()是将十六进制字符串转换为字节串，然后再用binascii.hexlify()将字节字符串转换为十六进制字符串。

    def xor_operation(self):
        number=self.current_page.findChild(QTextEdit, "xornumber")
        data=self.data.toPlainText()
        for i in range(len(data)):
            data=binascii.unhexlify(data[i])
            data=data^number
        self.browser.setText(data)
    
    def format_string(self):
        string=self.data.toPlainText()
        string=string.replace(" ","")
        string=string.replace("\n","")
        self.browser.setText(string)
        