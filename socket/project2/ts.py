#   服务端程序

from socket import *

IP = '0.0.0.0'
PORT = 50000
BUFLEN = 512

#  AF_INET表示网络层使用IP协议
#  SOCK_STREAM表示传输层使用TCP协议
listenSocket = socket(AF_INET, SOCK_STREAM)
listenSocket.bind((IP, PORT))

#  5表示最多5个客户端
listenSocket.listen(5)
print(f'服务启动, 在{PORT}端口等待客户端连接....')

#  此处开始阻塞
dataSocket, addr = listenSocket.accept()

print('接受一个客户端连接', addr)
while True:
    received = dataSocket.recv(BUFLEN)
    if not received:
        break
    info = received.decode()
    print(f"接收到对方信息{info}")
    dataSocket.send(f"服务器接收到了信息{info}".encode())

dataSocket.close()
listenSocket.close()
