
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import socket
import time

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui.ui', self)
        self.serverMACAddress = 'e8:48:b8:c8:20:00'
        self.port = 7
        self.s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        self.win_vk.clicked.connect(self.win)
        self.f1.clicked.connect(self.connectKeyboard)

    def connectKeyboard(self):
        self.s.connect((self.serverMACAddress, self.port))

    def win(self):
        self.s.send(bytes(str("win"), 'UTF-8'))
        self.s.recv(1024)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())