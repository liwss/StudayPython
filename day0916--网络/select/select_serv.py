# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/10/10 10:27
# @describe : 


import select
import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 55555))
server.listen(5)
# print 'server:', server
inputs = [server]   # 存储套接字，即被监听的套接字列表

while True:

    # 调用 select 函数，阻塞等待，监听服务端套接字及客户端套接字
    # select参数 arg1：检测这个列表中的套接字是否可读
    #            arg2:检测这个列表中的套接字是否可写
    #            arg3:检测这个列表中的套接字是否产生异常
    #            arg4:检测循环时间单位秒
    readable, writeable, exceptional = select.select(inputs, [], [], 1)
    print readable
    # 数据抵达，循环
    for sock in readable:
        # print 'sock:', sock
        # 监听到有新的连接
        if sock is server:  # 服务端套接字被触发，说明是有新的客户端连接过来
            conn, addr = server.accept()
            # select 监听的socket
            inputs.append(conn)  # 加入客户端套接字到列表
        # 有数据到达
        else:               # 客户端套接字被触发，说明有数据传输
            # 读取客户端连接发送的数据
            try:
                data = sock.recv(1024)  # sock即被触发的套接字
                # print 'sock1:', sock
            except Exception as e:
                print '客户端断开:',e
                # 移除select监听的socket
                inputs.remove(sock)
                sock.close()
            else:
                if len(data) > 0:
                    print data
                    sock.send(data)
                else:
                    inputs.remove(sock)
                    sock.close()
    # print inputs

server.close()

