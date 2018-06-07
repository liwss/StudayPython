# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/6/5 10:01
# @describe : SocketServer TCP服务器

from time import ctime
from SocketServer import TCPServer as TCP, StreamRequestHandler as SRH

host = ''
port = 8888
ADDR = (host, port)


class MyRequestHandler(SRH):
    def handle(self):
        print '...connected form:', self.client_address
        self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))

tcpServ = TCP(ADDR, MyRequestHandler)
print 'waiting for connection ...'
tcpServ.serve_forever()
