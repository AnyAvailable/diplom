

import socket
import keyboard

hostMACAddress = 'e8:48:b8:c8:20:00' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 5 # 3 is an arbitrary choice. However, it must match the port used by the client.
backlog = 1
size = 1024
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACAddress,port))
s.listen(backlog)
keyboard.release("win")
client, address = s.accept()

def receiveAndExecute():
    data = client.recv(size)
    if data:
        keys = str(data.decode("utf-8"))
        keyboard.press(keys)
        client.send(data)
        keyboard.release(keys)
        print(bytes.decode(data))

while 1:
    try:
        receiveAndExecute()
    except ConnectionAbortedError:
        client, address = s.accept()
"""except:	
    print("Closing socket")	
    print(Exception)
    client.close()
    s.close()"""