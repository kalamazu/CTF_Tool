import base64
from PyQt5.QtWidgets import QTextEdit, QPushButton,QLabel
import Ui_untitled

class MainWindow(Ui_untitled.Ui_MainWindow):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.char_map = None
        self.base64_default_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        
        self.setup_connections()

    def setup_connections(self):
        
        self.current_page = self.ui.stackedWidget.currentWidget()
        if self.current_page:
            button = self.current_page.findChild(QPushButton, "pbconfirm")
            if button:
                button.clicked.connect(lambda:self.solution())
            else:
                print("Button 'pbconfirm' not found!")
        else:
            print("Current page is not found!")

    def solution(self):
        self.current_page = self.ui.stackedWidget.currentWidget()
        self.tips=self.current_page.findChild(QLabel, "tips")
        if self.current_page:
            ciphertext_edit = self.current_page.findChild(QTextEdit, "ciphertext")
            comparetable_edit = self.current_page.findChild(QTextEdit, "comparetable")
            plaintext_edit = self.current_page.findChild(QTextEdit, "plaintext")
            
            if ciphertext_edit and comparetable_edit and plaintext_edit:
                self.ciphertext = ciphertext_edit.toPlainText()
                self.comparetable = comparetable_edit.toPlainText()
                self.plaintext = plaintext_edit.toPlainText()
                
                if self.comparetable:
                 try:
                    if len(self.comparetable) < len(self.base64_default_table):
                        self.comparetable = str.ljust(self.comparetable, len(self.base64_default_table), '?')
                        self.tips.setText(f'Length not enough, padding:\n{self.comparetable}')
                    self.char_map = str.maketrans(self.comparetable, self.base64_default_table)
                 except:
                    self.tips.setText("编码表过长！")
                    
                else:
                    self.char_map = str.maketrans(self.base64_default_table, self.base64_default_table)

                if self.plaintext == '' and self.ciphertext == '':
                    self.tips.setText("请输入明文或者密文")
                    
                    return 

                if self.plaintext == '':
                    try:
                        result = base64.b64decode(self.ciphertext.translate(self.char_map))
                        self.plaintext = result.decode('utf-8')
                        plaintext_edit.setPlainText(self.plaintext)
                    except:
                        self.tips.setText("密文格式不正确")
                        
                         
                else:
                 try:
                    encoded = base64.b64encode(self.plaintext.encode('utf-8'))
                    if self.char_map:
                        result = encoded.decode('utf-8').translate(self.char_map)
                    else:
                        result = encoded.decode('utf-8')
                    ciphertext_edit.setPlainText(result)
                 except:
                     self.tips.setText("明文格式不正确")
            else:
                print("One or more text edits not found!")
