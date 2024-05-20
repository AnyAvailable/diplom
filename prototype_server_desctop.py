import socket
import keyboard
import sys

hostMACAddress = 'e8:48:b8:c8:20:00' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 7 # 3 is an arbitrary choice. However, it must match the port used by the client.
backlog = 1
size = 1024
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACAddress,port))
s.listen(backlog)

while 1:
    client, address = s.accept()
    while 1:
        try:
            data = client.recv(size)
        except ConnectionError:
            break
        if not data: break
        if data:
            keys = str(data.decode("utf-8"))
            keyboard.press(keys)
            client.send(data)
            keyboard.release(keys)
            print(bytes.decode(data))
s.close()
sys.exit(0)