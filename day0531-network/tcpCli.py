# coding=utf-8

from socket import *
from time import ctime

host = '127.0.0.1'   # 目标主机ip
port = 10086          # 目标主机port
bufsize = 1024       # 缓存大小
ADDr = (host, port)  

s = socket(AF_INET, SOCK_STREAM) # 创建tcp套接字
s.connect(ADDr)                  # 和目标主机建立连接

while True:
    date = raw_input('>>')        
    if not date:
        break 
    print date
    s.send(date)              # 发送消息
    date = s.recv(bufsize)    # 接收消息
    if not date:
        break
    print '<<' + date
s.close()



