# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/17 15:07
# @describe : 

# 创建一个请求处理类，并且这个类要继承BaseRequestHandler,并且还有重写父亲类里的handle()
# 实例化TCPServer ，并且传递server ip 和 创建的请求处理类 给这个TCPServer
# serve_forever() #处理多个一个请求，永远执行

import socketserver


class MyTcpServer(socketserver.BaseRequestHandler):

    def handle(self):       # 重写父类方法，实现自身业务处理
        while True:
            try:                                        # 异常处理，防止客户端断开导致服务端异常
                data = self.request.recv(1024).strip()
                print (self.client_address[0], data)
                self.request.send(data.upper())
            except Exception as e:
                print e, "客户端[%s:%s]断开连接" % (self.client_address[0], self.client_address[1])
                break

if __name__ == '__main__':
    # tcpServer = socketserver.TCPServer(('127.0.0.1', 55555), MyTcpServer)
    #  TCPServer接收一个客户端请求

    tcpServer = socketserver.ThreadingTCPServer(('127.0.0.1', 55555), MyTcpServer)
    # ThreadingTCPServer接收多个客户端连接，多线程模型,还有多进程的模型ForkingTCPServer
    tcpServer.serve_forever()
    tcpServer.shutdown()
    tcpServer.server_close()
