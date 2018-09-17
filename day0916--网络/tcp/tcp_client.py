# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/16 16:21
# @describe : tcp客户端

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 55555))
while True:
    data = raw_input("请输入要发送的内容:")
    if not data:
        break
    s.send(data)
    print ("客户端发送数据[%s]" % data)
    data = s.recv(1024)
    print ("客户端即将接收服务端数据包大小[%s]" % data)
    s.send("数据包大小已接收")   # 给服务端返回数据包大小已接收，从而服务端发送数据体
    recvsize = data     # 接收服务端发过来的数据包大小
    datasize = 0
    recvdata = ''
    while datasize < int(recvsize):     # 如果实际接收<真实大小，就循环取数据
        data = s.recv(1)
        datasize += len(data)
        recvdata += data
    print ("客户端真实接收数据[%s],大小[%s]" % (recvdata, datasize))
s.close()
