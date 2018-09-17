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
        print ("服务端接收数据[%s]" % data)
        datasize = len(data)
        print ("服务端发送数据大小[%s]" % datasize)
        sd.send(str(datasize))      # 先发送接收方数据包的大小
        ack = sd.recv(1024)         # 增加一个数据包大小发送后的响应确认，确认客户端接收到了包大小再发送数据
        print ("收到客户端ack确认[%s]:" % ack)
        sd.send(data.upper())       # 再发送真实报文数据
        print ("服务端发送数据[%s]" % data.upper())
    sd.close()
s.close()
