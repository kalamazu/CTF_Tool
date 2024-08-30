import base64
from PyQt5.QtWidgets import QTextEdit, QPushButton,QLabel
import Ui_untitled

class MainWindow(Ui_untitled.Ui_MainWindow):
    def __init__(self,ui):
        super().__init__()
        self.ui = ui  
        self.setup_connections()