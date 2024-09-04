#coding = 'utf-8'
#GUI修改代码
import sys
from PyQt5 import QtWidgets
import Ui_untitled
import base64handler
import Stringhandler

def pbBase64buttonClicked(ui: Ui_untitled.Ui_MainWindow) -> None:
    ui.stackedWidget.setCurrentIndex(0)
    base64handle = base64handler.MainWindow(ui)

def pbStringbuttonClicked(ui: Ui_untitled.Ui_MainWindow)->None:
    ui.stackedWidget.setCurrentIndex(1)
    Stringhandle=Stringhandler.MainWindow(ui)

def pbZ3buttonClicked(ui: Ui_untitled.Ui_MainWindow) -> None:
    ui.stackedWidget.setCurrentIndex(2)
    Stringhandle=Stringhandler.MainWindow(ui)

def pbangrbuttonClicked(ui: Ui_untitled.Ui_MainWindow) -> None:
    pass



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 创建QApplication对象
    MainWindow = QtWidgets.QMainWindow()  # 创建QMainWindow对象
    screen = app.primaryScreen()  # 获取屏幕
    width=screen.size().width()*0.5
    height=screen.size().height()*0.5
    MainWindow.resize(int(width),int(height))  # 设置窗口大小
    ui = Ui_untitled.Ui_MainWindow()  # 创建一个UI对象
    ui.setupUi(MainWindow)  # 设置主窗口的UI
    ui.stackedWidget.setCurrentIndex(0)  # 设置初始页面


    # Connect buttons after setting up UI
    ui.pbBase64.clicked.connect(lambda: pbBase64buttonClicked(ui))
    ui.pbZ3.clicked.connect(lambda: pbZ3buttonClicked(ui))
    ui.pbangr.clicked.connect(lambda: pbangrbuttonClicked(ui))
    ui.pbString.clicked.connect(lambda: pbStringbuttonClicked(ui))

    MainWindow.setWindowTitle("CTF_Tools")  # 设置窗口标题
    MainWindow.show()  # 展示窗口
    sys.exit(app.exec_())  # 启动事件循环，返回一个退出状态
