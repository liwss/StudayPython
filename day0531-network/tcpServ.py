# coding=utf-8

from socket import *
from time import ctime

host = ''
port = 8888    	 # 端口，int型
bufsize = 1024	 # 缓存大小，int型
addr = (host, port)

s = socket(AF_INET, SOCK_STREAM) # 创建tcp套接字
s.bind(addr)     # 绑定监听主机ip(服务端可谓空) port 
s.listen(5)      # 连接在转发或被拒绝之前，传入连接请求的最大数

while True:
	print 'waiting for connect ......'
	tcpcli, addr = s.accept() # 默认阻塞，直到新的连接到来，返回新的临时套接字和客户端请求信息
	print '...connected from:',addr

	while True:
		date = tcpcli.recv(bufsize) # 接收客户端请求数据
		if not date:
			break
		tcpcli.send('[%s] %s' % (ctime(), date))
		print '[%s] %s' % (ctime(), date)
	tcpcli.close()
s.close()

