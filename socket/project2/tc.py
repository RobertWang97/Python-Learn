#  客户端程序
from socket import *

IP = "127.0.0.1"
SERVER_PORT = 50000
BUFLEN = 1024

dataSocket = socket(AF_INET, SOCK_STREAM)
dataSocket.connect((IP, SERVER_PORT))
while True:
    toSend = input('>> ')
    if toSend=="":
        break

    dataSocket.send(toSend.encode())
    received = dataSocket.recv(BUFLEN)
    if not received:
        break

    print(received.decode())

dataSocket.close()
