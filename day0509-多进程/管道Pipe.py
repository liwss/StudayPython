# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/19 15:48
# @describe : 

import time
import multiprocessing


def test(conn2):
    while True:
        time.sleep(1)
        conn2.send("lws")
        print conn2.recv()


if __name__ == '__main__':
    conn1, conn2 = multiprocessing.Pipe()  # 实例Pipe对象，返回两个连接对象,表示管道两端
    p = multiprocessing.Process(target=test, args=(conn2,))  # 创建子进程，传入管道一端的连接对象
    p.start()
    while True:
        time.sleep(1)
        conn1.send("820")      # 发送内容到管道
        print conn1.recv()     # 接收管道内容

