# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/17 15:46
# @describe : 


import socket

address = '127.0.0.1'
port = 55555
ADDR = (address, port)
bufsize = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)
while True:
    send_data = raw_input("please input >>")
    s.send(send_data)
    recv_data = s.recv(bufsize)
    print ("收到服务端返回数据[%s]" % recv_data)
s.close()