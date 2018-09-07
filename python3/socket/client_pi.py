# -*- coding: utf-8 -*-
# client端
#  Client.py
import socket

address = ('172.18.250.190', 33333)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.connect(address)

s.sendall("here is client")
data = s.recv(1024)
print (data)
s.close()