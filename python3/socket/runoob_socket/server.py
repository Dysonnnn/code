#-*- coding: UTF-8 -*-
# 文件名：server.py
#服务端自己的监听地址和客户端书写的服务端地址形式必须要完全对应,
#或者服务端地址写成空字符串”“形式,表示所有可用地址。程序才能正常传输文件。
import socket             # 导入 socket 模块

s = socket.socket()         # 创建 socket 对象
#host = socket.gethostname() # 获取本地主机名
host = ''
port = 1234                # 设置端口
s.bind((host, port))        # 绑定端口
#####################################

import os
os.system(u"dir")
#####################################

s.listen(5)                 # 等待客户端连接
while True:
    c, addr = s.accept()     # 建立客户端连接。
    print '连接地址：', addr
    #send_buf[100] = {0}
    c.send('欢迎访问菜鸟教程！')
    #c.send(send_buf[0])
    c.recv(1024)
    c.close()                # 关闭连接
