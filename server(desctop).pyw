"""
A simple Python script to receive messages from a client over
Bluetooth using Python sockets (with Python 3.3 or above).
"""
#imports#

import socket
import keyboard
import os

#imports#



#initialisation block#

"""programPath = "\'C:/Users/egoro/OneDrive/Рабочий стол/diplom/dist/server(desctop)/server(desctop).exe\'"
print(programPath)
os.system(f'cd {programPath}')
startUp = "%appdata%/Microsoft/Windows/Start Menu/Programs/Startup/server(desctop).exe"
#os.system(f"move {programPath} {startUp}")"""

#initialisation block#

#findingBtMacAdress#
text = os.popen('wmic nic list brief /format:csv').read()
valuelist = text.split(",")
hostMACAddress = valuelist[valuelist.index("BthPan")-3] # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
#findingBtMacAdress#




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
            print(bytes.decode(data))
            keyboard.press(bytes.decode(data))
            keyboard.release(bytes.decode(data))
            client.send(data)
except:	
    print("Closing socket")	
    client.close()
    s.close()