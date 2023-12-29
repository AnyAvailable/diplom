"""
A simple Python script to send messages to a sever over Bluetooth using
Python sockets (with Python 3.3 or above).
"""

import socket
import keyboard

def keyBoardListener() -> str:
    memory = []
    buffer = ''
    scancodeOut = ''
    
    while 1:
        buffer = keyboard.read_key()
        
        
        if keyboard.is_pressed(buffer):
            
            if memory.count(buffer) == 0:
                memory.append(buffer)
        
        
        if not (keyboard.is_pressed(buffer)):
            
            for key in memory:
                scancodeOut += key + ' '
            
            scancodeOut = scancodeOut.rstrip().replace(' ', '+')
            break
        
        return scancodeOut

serverMACAddress = 'e8:48:b8:c8:20:00'
port = 3
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))
while 1:
    
    s.send(bytes(keyBoardListener(), 'UTF-8'))
s.close()