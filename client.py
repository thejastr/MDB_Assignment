import socket

ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004

print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))

res = ClientMultiSocket.recv(1024)
Input=""
while Input!='bye':
    Input = input('Type your message: ')
    ClientMultiSocket.send(str.encode(Input))

ClientMultiSocket.close()
