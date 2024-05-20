"""
A simple Python script to send messages to a sever over Bluetooth using
Python sockets (with Python 3.3 or above).
"""

import socket

def keyBoardListener() -> str:
    memory = []
    buffer = ''
    scancodeOut = '123'
        
    return scancodeOut

serverMACAddress = 'e8:48:b8:c8:20:00'
port = 5
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))
while 1:
    
    s.send(bytes(keyBoardListener(), 'UTF-8'))
s.close()