import socket
import os
from _thread import *

ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Socket is listening..')
ServerSideSocket.listen(5)

def client(connection,address):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048)
        print("Msg from",address," : ",data.decode('utf-8'))
        if data.decode('utf-8')=="bye":
            break
    connection.close()

while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(client, (Client,address ))
ServerSideSocket.close()
