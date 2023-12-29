"""
A simple Python script to send messages to a sever over Bluetooth using
Python sockets (with Python 3.3 or above).
"""

import socket
import keyboard
memory = []
serverMACAddress = 'e8:48:b8:c8:20:00'
port = 4
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))
while 1:
    buffer = keyboard.read_key()
    
    

    if keyboard.is_pressed(buffer):
        if memory.count(buffer) == 0:
            memory.append(buffer)
            memory.append('+')
    elif not keyboard.is_pressed(buffer):
        text = ""
        try:
            memory.pop()
        except IndexError:
            continue
        for key in memory:
            text += key
        s.send(bytes(text, 'UTF-8'))
        memory.clear()
s.close()