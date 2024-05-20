
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import socket
import time

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui.ui', self)
        self.win.clicked.connect(self.win)

    def win(self):
        serverMACAddress = 'e8:48:b8:c8:20:00'
        port = 5
        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        s.connect((serverMACAddress,port))
        while 1:
    
            s.send(bytes(str(keyBoardListener()), 'UTF-8'))
            data = s.recv(1024)
            print(bytes.decode(data, "utf-8") + "pressed")
            time.sleep(1)
            break
        s.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())


def keyBoardListener() -> str:
    memory = "win"        
    return memory
    


