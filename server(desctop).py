"""
A simple Python script to receive messages from a client over
Bluetooth using Python sockets (with Python 3.3 or above).
"""

import socket
import keyboard

hostMACAddress = 'e8:48:b8:c8:20:00' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 4 # 3 is an arbitrary choice. However, it must match the port used by the client.
backlog = 1
size = 1024
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACAddress,port))
s.listen(backlog)
try:
    client, address = s.accept()
    while 1:
        data = client.recv(size)
        if data:
            print(list(bytes.decode(data)))
            keyboard.play(list(bytes.decode(data)))
            client.send(list(bytes.decode(data)))
except:	
    print("Closing socket")	
    client.close()
    s.close()