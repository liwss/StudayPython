# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/16 16:33
# @describe : 

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 55555))
s.listen(5)
while True:
    sd, addr = s.accept()
    while True:
        data = sd.recv(1024)
        if not data:
            break
        print ("服务端:", data)
        datasize = len(data)
        sd.send(str(datasize))      # 先发送接收方数据包的大小
        print (datasize)
        sd.send(data.upper())       # 再发送真实报文数据
        print (data.upper())
    sd.close()
s.close()
