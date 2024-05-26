
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
        self.connected = False
        self.memory = ""
        self.combo = self.comboenable_rb
        self.port_spinbox.textChanged.connect(self.portChange)
        self.mac_textarea.textChanged.connect(self.macChange)
        self.esc_vk.clicked.connect(self.esc)
        self.f1_vk.clicked.connect(self.f1)
        self.f2_vk.clicked.connect(self.f2)
        self.f3_vk.clicked.connect(self.f3)
        self.f4_vk.clicked.connect(self.f4)
        self.f5_vk.clicked.connect(self.f5)
        self.f6_vk.clicked.connect(self.f6)
        self.f7_vk.clicked.connect(self.f7)
        self.f8_vk.clicked.connect(self.f8)
        self.f9_vk.clicked.connect(self.f9)
        self.f10_vk.clicked.connect(self.f10)
        self.f11_vk.clicked.connect(self.f11)
        self.f12_vk.clicked.connect(self.f12)
        self.del_vk.clicked.connect(self.delete)
        self.tilda_vk.clicked.connect(self.tilda)
        self.one_vk.clicked.connect(self.one)
        self.two_vk.clicked.connect(self.two)
        self.three_vk.clicked.connect(self.three)
        self.four_vk.clicked.connect(self.four)
        self.five_vk.clicked.connect(self.five)
        self.six_vk.clicked.connect(self.six)
        self.seven_vk.clicked.connect(self.seven)
        self.eight_vk.clicked.connect(self.eight)
        self.nine_vk.clicked.connect(self.nine)
        self.zero_vk.clicked.connect(self.zero)
        self.minus_vk.clicked.connect(self.minus)
        self.plus_vk.clicked.connect(self.plus)
        self.backspace_vk.clicked.connect(self.backspace)
        self.ins_vk.clicked.connect(self.ins)
        self.home_vk.clicked.connect(self.home)
        self.pgup_vk.clicked.connect(self.pgup)
        self.del_vk.clicked.connect(self.delete)
        self.end_vk.clicked.connect(self.end)
        self.pgdn_vk.clicked.connect(self.pgdn)
        self.tab_vk.clicked.connect(self.tab)
        self.q_vk.clicked.connect(self.q)
        self.w_vk.clicked.connect(self.w)
        self.e_vk.clicked.connect(self.e)
        self.r_vk.clicked.connect(self.r)
        self.t_vk.clicked.connect(self.t)
        self.y_vk.clicked.connect(self.y)
        self.u_vk.clicked.connect(self.u)
        self.i_vk.clicked.connect(self.i)
        self.o_vk.clicked.connect(self.o)
        self.p_vk.clicked.connect(self.p)
        self.leftbracket_vk.clicked.connect(self.leftbracket)
        self.rightbracket_vk.clicked.connect(self.rightbracket)
        self.a_vk.clicked.connect(self.a)
        self.s_vk.clicked.connect(self.sl)
        self.d_vk.clicked.connect(self.d)
        self.f_vk.clicked.connect(self.f)
        self.g_vk.clicked.connect(self.g)
        self.h_vk.clicked.connect(self.h)
        self.j_vk.clicked.connect(self.j)
        self.k_vk.clicked.connect(self.k)
        self.l_vk.clicked.connect(self.l)
        self.zh_vk.clicked.connect(self.zh)
        self.commas_vk.clicked.connect(self.commas) #
        self.slash_vk.clicked.connect(self.slash)
        self.z_vk.clicked.connect(self.z)
        self.x_vk.clicked.connect(self.x)
        self.c_vk.clicked.connect(self.c)
        self.v_vk.clicked.connect(self.v)
        self.b_vk.clicked.connect(self.b)
        self.n_vk.clicked.connect(self.n)
        self.m_vk.clicked.connect(self.m)
        self.leftarrow_vk.clicked.connect(self.leftarrow)
        self.rightarrow_vk.clicked.connect(self.rightarrow)
        self.dot_vk.clicked.connect(self.dot)
        self.rightshift_vk.clicked.connect(self.rightshift)
        self.enter_vk.clicked.connect(self.enter)
        self.rightctrl_vk.clicked.connect(self.rightctrl)
        #self.list__vk.clicked.connect(self.list)
        #self.fn_vk.clicked.connect(self.fn)
        self.rightalt_vk.clicked.connect(self.rightalt)
        self.leftalt_vk.clicked.connect(self.leftalt)
        self.space_vk.clicked.connect(self.space)
        self.leftctrl_vk.clicked.connect(self.leftctrl)
        self.up_vk.clicked.connect(self.up)
        self.down_vk.clicked.connect(self.down)
        self.left_vk.clicked.connect(self.left)
        self.right_vk.clicked.connect(self.right)
        self.capslock_vk.clicked.connect(self.caps)
        self.capitalize = False
        self.win_vk.clicked.connect(self.win)
        self.r_vk.clicked.connect(self.r)
        self.connect_vk.clicked.connect(self.connectKeyboard)

    def connectKeyboard(self):
        if self.connected:
            try:
                self.s.close()
                self.connect_vk.setStyleSheet('#connect_vk{background: rgba(196,0,0,255)}')
                self.connect_vk.setText("CONNECT")
                self.connected = False
            except:
                pass
        else:
            try:
                self.s.connect((self.serverMACAddress, self.port))
                self.connect_vk.setStyleSheet('#connect_vk{background: rgba(0,196,0,255)}')
                self.connect_vk.setText("DISCONNECT")
                self.connected = True
            except:
                pass


    def portChange(self):
        self.port = self.port_spinbox.value()


    def macChange(self):
        self.serverMACAddress = self.mac_textarea.toPlainText()


    def esc(self):
        if self.combo.isChecked():
            self.memory += "esc+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("esc"), "utf-8"))
            self.s.recv(1024)

    
    def f1(self):
        if self.combo.isChecked():
            self.memory += "f1+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("f1"), "utf-8"))
            self.s.recv(1024)


    def f2(self):
        if self.combo.isChecked():
            self.memory += "f2+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("f2"), "utf-8"))
            self.s.recv(1024)


    def f3(self):
        if self.combo.isChecked():
            self.memory += "f3+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("f3"), "utf-8"))
            self.s.recv(1024)


    def f4(self):
        if self.combo.isChecked():
            self.memory += "f4+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("f4"), "utf-8"))
            self.s.recv(1024)


    def f5(self):
        if self.combo.isChecked():
            self.memory += "f5+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("f5"), "utf-8"))
            self.s.recv(1024)


    def f6(self):
        if self.combo.isChecked():
            self.memory += "f6+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("f6"), "utf-8"))
            self.s.recv(1024)


    def f7(self):
        if self.combo.isChecked():
            self.memory += "f7+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("f7"), "utf-8"))
            self.s.recv(1024)


    def f8(self):
        if self.combo.isChecked():
            self.memory += "f8+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("f8"), "utf-8"))
            self.s.recv(1024)


    def f9(self):
        if self.combo.isChecked():
            self.memory += "f9+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("f9"), "utf-8"))
            self.s.recv(1024)


    def f10(self):
        if self.combo.isChecked():
            self.memory += "f10+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("f10"), "utf-8"))
            self.s.recv(1024)


    def f11(self):
        if self.combo.isChecked():
            self.memory += "f11+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("f11"), "utf-8"))
            self.s.recv(1024)


    def f12(self):
        if self.combo.isChecked():
            self.memory += "f12+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("rf12"), "utf-8"))
            self.s.recv(1024)

    
    def delete(self):
        if self.combo.isChecked():
            self.memory += "del+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("del"), "utf-8"))
            self.s.recv(1024)


    def tilda(self):
        if self.combo.isChecked():
            self.memory += "~+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("~"), "utf-8"))
            self.s.recv(1024)


    def one(self):
        if self.combo.isChecked():
            self.memory += "1+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("1"), "utf-8"))
            self.s.recv(1024)


    def two(self):
        if self.combo.isChecked():
            self.memory += "2+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("2"), "utf-8"))
            self.s.recv(1024)

    
    def three(self):
        if self.combo.isChecked():
            self.memory += "3+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("3"), "utf-8"))
            self.s.recv(1024)


    def four(self):
        if self.combo.isChecked():
            self.memory += "4+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("4"), "utf-8"))
            self.s.recv(1024)


    def five(self):
        if self.combo.isChecked():
            self.memory += "5+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("5"), "utf-8"))
            self.s.recv(1024)


    def six(self):
        if self.combo.isChecked():
            self.memory += "6+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("6"), "utf-8"))
            self.s.recv(1024)


    def seven(self):
        if self.combo.isChecked():
            self.memory += "7+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("7"), "utf-8"))
            self.s.recv(1024)


    def eight(self):
        if self.combo.isChecked():
            self.memory += "8+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("8"), "utf-8"))
            self.s.recv(1024)


    def nine(self):
        if self.combo.isChecked():
            self.memory += "9+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("9"), "utf-8"))
            self.s.recv(1024)


    def zero(self):
        if self.combo.isChecked():
            self.memory += "0+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("0"), "utf-8"))
            self.s.recv(1024)


    def minus(self):
        if self.combo.isChecked():
            self.memory += "minus+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("minus"), "utf-8"))
            self.s.recv(1024)


    def plus(self):
        if self.combo.isChecked():
            self.memory += "plus+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("plus"), "utf-8"))
            self.s.recv(1024)

    
    def backspace(self):
        if self.combo.isChecked():
            self.memory += "backspace+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("backspace"), "utf-8"))
            self.s.recv(1024)

    
    def tab(self):
        if self.combo.isChecked():
            self.memory += "tab+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("tab"), "utf-8"))
            self.s.recv(1024)


    def q(self):
        if self.combo.isChecked():
            self.memory += "q+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("q"), "utf-8"))
            self.s.recv(1024)


    def w(self):
        if self.combo.isChecked():
            self.memory += "w+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("w"), "utf-8"))
            self.s.recv(1024)


    def e(self):
        if self.combo.isChecked():
            self.memory += "e+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("e"), "utf-8"))
            self.s.recv(1024)
            
    
    def r(self):
        if self.combo.isChecked():
            self.memory += "r+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("r"), "utf-8"))
            self.s.recv(1024)


    def t(self):
        if self.combo.isChecked():
            self.memory += "t+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("t"), "utf-8"))
            self.s.recv(1024)


    def y(self):
        if self.combo.isChecked():
            self.memory += "y+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("y"), "utf-8"))
            self.s.recv(1024)


    def u(self):
        if self.combo.isChecked():
            self.memory += "u+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("u"), "utf-8"))
            self.s.recv(1024)


    def i(self):
        if self.combo.isChecked():
            self.memory += "i+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("i"), "utf-8"))
            self.s.recv(1024)


    def o(self):
        if self.combo.isChecked():
            self.memory += "o+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("o"), "utf-8"))
            self.s.recv(1024)


    def p(self):
        if self.combo.isChecked():
            self.memory += "p+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("p"), "utf-8"))
            self.s.recv(1024)


    def leftbracket(self):
        if self.combo.isChecked():
            self.memory += "[+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("["), "utf-8"))
            self.s.recv(1024)


    def rightbracket(self):
        if self.combo.isChecked():
            self.memory += "]+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("]"), "utf-8"))
            self.s.recv(1024)


    def enter(self):
        if self.combo.isChecked():
            self.memory += "enter+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("enter"), "utf-8"))
            self.s.recv(1024)


    def caps(self):
        self.s.send(bytes(str("capslock"), "utf-8"))
        self.s.recv(1024)


    def a(self):
        if self.combo.isChecked():
            self.memory += "a+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("a"), "utf-8"))
            self.s.recv(1024)


    def sl(self):
        if self.combo.isChecked():
            self.memory += "s+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("s"), "utf-8"))
            self.s.recv(1024)


    def d(self):
        if self.combo.isChecked():
            self.memory += "d+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("d"), "utf-8"))
            self.s.recv(1024)


    def f(self):
        if self.combo.isChecked():
            self.memory += "f+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("f"), "utf-8"))
            self.s.recv(1024)


    def g(self):
        if self.combo.isChecked():
            self.memory += "g+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("g"), "utf-8"))
            self.s.recv(1024)


    def h(self):
        if self.combo.isChecked():
            self.memory += "h+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("h"), "utf-8"))
            self.s.recv(1024)


    def j(self):
        if self.combo.isChecked():
            self.memory += "j+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("j"), "utf-8"))
            self.s.recv(1024)


    def k(self):
        if self.combo.isChecked():
            self.memory += "k+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("k"), "utf-8"))
            self.s.recv(1024)


    def l(self):
        if self.combo.isChecked():
            self.memory += "l+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("l"), "utf-8"))
            self.s.recv(1024)


    def zh(self):
        if self.combo.isChecked():
            self.memory += "ж+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("ж"), "utf-8"))
            self.s.recv(1024)


    def commas(self):
        if self.combo.isChecked():
            self.memory += "э+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("э"), "utf-8"))
            self.s.recv(1024)


    def slash(self):
        if self.combo.isChecked():
            self.memory += "|+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("|"), "utf-8"))
            self.s.recv(1024)


    def shift(self):
        if self.combo.isChecked():
            self.memory += "left shift+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("left shift"), "utf-8"))
            self.s.recv(1024)


    def z(self):
        if self.combo.isChecked():
            self.memory += "z+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("z"), "utf-8"))
            self.s.recv(1024)


    def x(self):
        if self.combo.isChecked():
            self.memory += "x+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("x"), "utf-8"))
            self.s.recv(1024)


    def c(self):
        if self.combo.isChecked():
            self.memory += "c+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("c"), "utf-8"))
            self.s.recv(1024)


    def v(self):
        if self.combo.isChecked():
            self.memory += "v+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("v"), "utf-8"))
            self.s.recv(1024)


    def b(self):
        if self.combo.isChecked():
            self.memory += "b+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("b"), "utf-8"))
            self.s.recv(1024)


    def n(self):
        if self.combo.isChecked():
            self.memory += "n+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("n"), "utf-8"))
            self.s.recv(1024)


    def m(self):
        if self.combo.isChecked():
            self.memory += "m+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("m"), "utf-8"))
            self.s.recv(1024)


    def leftarrow(self):
        if self.combo.isChecked():
            self.memory += "б+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("б"), "utf-8"))
            self.s.recv(1024)

    
    def rightarrow(self):
        if self.combo.isChecked():
            self.memory += "ю+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("ю"), "utf-8"))
            self.s.recv(1024)


    def dot(self):
        if self.combo.isChecked():
            self.memory += "?+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("?"), "utf-8"))
            self.s.recv(1024)


    def rightshift(self):
        if self.combo.isChecked():
            self.memory += "right shift+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("right shift"), "utf-8"))
            self.s.recv(1024)


    def leftctrl(self):
        if self.combo.isChecked():
            self.memory += "left control+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("|"), "utf-8"))
            self.s.recv(1024)


    def leftalt(self):
        if self.combo.isChecked():
            self.memory += "left alt+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("left alt"), "utf-8"))
            self.s.recv(1024)


    def space(self):
        if self.combo.isChecked():
            self.memory += "space+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("space"), "utf-8"))
            self.s.recv(1024)

    
    def rightalt(self):
        if self.combo.isChecked():
            self.memory += "right alt+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("right alt"), "utf-8"))
            self.s.recv(1024)


    def rightctrl(self):
        if self.combo.isChecked():
            self.memory += "right control+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("right control"), "utf-8"))
            self.s.recv(1024)


    def left(self):
        if self.combo.isChecked():
            self.memory += "left+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("left"), "utf-8"))
            self.s.recv(1024)

    
    def right(self):
        if self.combo.isChecked():
            self.memory += "right+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("right"), "utf-8"))
            self.s.recv(1024)


    def up(self):
        if self.combo.isChecked():
            self.memory += "up+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("up"), "utf-8"))
            self.s.recv(1024)


    def down(self):
        if self.combo.isChecked():
            self.memory += "sown+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("down"), "utf-8"))
            self.s.recv(1024)


    def win(self):
        if self.combo.isChecked():
            self.memory += "win+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("win"), "utf-8"))
            self.s.recv(1024)


    def prtsc(self):
        if self.combo.isChecked():
            self.memory += "printscreen+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("printscreen"), "utf-8"))
            self.s.recv(1024)


    def pause(self):
        if self.combo.isChecked():
            self.memory += "pause+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("pause"), "utf-8"))
            self.s.recv(1024)


    def scrlock(self):
        if self.combo.isChecked():
            self.memory += "scroll lock+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("scroll lock"), "utf-8"))
            self.s.recv(1024)


    def ins(self):
        if self.combo.isChecked():
            self.memory += "insert+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("insert"), "utf-8"))
            self.s.recv(1024)


    def home(self):
        if self.combo.isChecked():
            self.memory += "home+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("home"), "utf-8"))
            self.s.recv(1024)


    def pgup(self):
        if self.combo.isChecked():
            self.memory += "page up+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("page up"), "utf-8"))
            self.s.recv(1024)

    
    def end(self):
        if self.combo.isChecked():
            self.memory += "end+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("end"), "utf-8"))
            self.s.recv(1024)


    def pgdn(self):
        if self.combo.isChecked():
            self.memory += "page down+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("page down"), "utf-8"))
            self.s.recv(1024)


    def numlock(self):
        if self.combo.isChecked():
            self.memory += "numlock+"
        elif not self.combo.isChecked() and self.memory:
            try:
                self.memory = self.memory[:-1]
                self.s.send(bytes(self.memory, "utf-8"))
                self.s.recv(1024)
                self.memory = ""
            except:
                pass
        else:
            self.s.send(bytes(str("numlock"), "utf-8"))
            self.s.recv(1024)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())