# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/10/11 10:46
# @describe : epoll版服务器，不支持windows

import socket
import select

# 创建套接字
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 设置可以重复使用绑定的信息
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

# 绑定本机信息
s.bind(("127.0.0.1", 55555))

# 变为被动
s.listen(10)

# 创建一个epoll对象
epoll = select.epoll()

# 测试，用来打印套接字对应的文件描述符
# print s.fileno()
# print select.EPOLLIN|select.EPOLLET

# 注册事件到epoll中
# epoll.register(fd[, eventmask])
# 注意，如果fd已经注册过，则会发生异常
# 将创建的套接字添加到epoll的事件监听中
# s.fileno() 把对象s转换成文件描述符fd(正整数)
epoll.register(s.fileno(), select.EPOLLIN|select.EPOLLET)


connections = {}
addresses = {}

# 循环等待客户端的到来或者对方发送数据
while True:

    # epoll 进行 fd 扫描的地方 -- 未指定超时时间则为阻塞等待
    epoll_list = epoll.poll()

    # 对事件进行判断
    for fd, events in epoll_list:

        # print fd
        # print events

        # 如果是socket创建的套接字被激活
        if fd == s.fileno():
            conn, addr=s.accept()

            print('有新的客户端到来%s'%str(addr))

            # 将 conn 和 addr 信息分别保存起来
            connections[conn.fileno()] = conn
            addresses[conn.fileno()] = addr

            # 向 epoll 中注册 连接 socket 的 可读 事件
            epoll.register(conn.fileno(), select.EPOLLIN | select.EPOLLET)

        elif events == select.EPOLLIN:
            # 从激活 fd 上接收
            recvData = connections[fd].recv(1024)

            if len(recvData)>0:
                print('recv:%s'%recvData)
            else:
                # 从 epoll 中移除该 连接 fd
                epoll.unregister(fd)

                # server 侧主动关闭该 连接 fd
                connections[fd].close()

                print("%s---offline---"%str(addresses[fd]))
