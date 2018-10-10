# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/10/9 13:54
# @describe : 

import socket

ADDRESS = ('127.0.0.1', 55555)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDRESS)
while True:
    data = raw_input("please input sendmsg >")
    s.send(data)
    try:
        data = s.recv(1024)
        print "接收数据:", data
    except:
        pass
s.close()