# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/10/8 14:38
# @describe :
# 单进程非阻塞服务端原理
# 1：由于recv接收数据时会发生IO阻塞，其他客户端连接时服务端就无法处理
# 2：使用setblocking(False)把sokcet变为非阻塞，就不存在以上情况
# 3：但需要自己记录客户端信息和移除客户端信息

import socket

ADDRESS = ('127.0.0.1', 55555)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 快速端口复用，解决2msl问题
s.bind(ADDRESS)     # 绑定本地ip及端口
s.listen(10)        # 将socket变为监听(被动)套接字
s.setblocking(False)    # 设置socket为非阻塞
clientAddrList = []     # 用来报存所有的已连接的客户端信息

while True:
    try:
        sd, addr = s.accept()   # 等待一个新的客户端到来(即完成3次握手操作的客户端)
        print sd, addr
    except:
        pass
    else:                   # 如果没有异常发生走else分支
        sd.setblocking(False)
        clientAddrList.append((sd, addr))

    for sd, addr in clientAddrList:
        try:
            data = sd.recv(1024)
        except:
            pass
        else:
            if len(data) > 0:
                print "接收的数据:", data
                sd.send(data.upper())
            else:
                sd.close()
                clientAddrList.remove((sd, addr))
s.close()



