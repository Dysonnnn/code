# -*-coding:utf-8 -*-
#   Server端
#   Server.py
import socket

HOST = ''
PORT = 33333
ADDR = (HOST,PORT)
#  AF_INET 表示连接使用ipv4地址族  SOCK_STREAM表示用流式套接字
tcpSerSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpSerSock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# 将套接字绑定该地址
tcpSerSock.bind(ADDR)
# 参数1表示阻塞模式  0表示非阻塞模式  默认为阻塞模式
tcpSerSock.setblocking(1)
# 开始监听TCP传入连接。参数指定在拒绝连接之前，操作系统可以挂起的最大连接数量。
tcpSerSock.listen(5)

print ("Waiting connect...")
# tcpCliSock 是该链接的套接字，addr表示对方的地址
tcpCliSock, addr = tcpSerSock.accept()
# 设置超时时间
tcpCliSock.settimeout(20.0)
print ('...connected from', addr)
# recv（param）用于接收对方发送的数据 param为缓冲区大小
data = tcpCliSock.recv(1024)
print (data)
tcpCliSock.sendall("here is server")
# 关闭套接字
tcpCliSock.close()