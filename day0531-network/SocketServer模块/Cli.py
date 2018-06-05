# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/6/5 10:18
# @describe : SocketServer TCP客户端

from socket import *

host = '127.0.0.1'
port = 8888
bufsize = 1024
ADDR = (host, port)

while True:
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(ADDR)
    date = raw_input('>>')
    if not date:
        break
    s.send('%s\r\n' % date)
    date = s.recv(bufsize)
    if not date:
        break
    print date.strip()
    s.close()







