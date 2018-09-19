# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/19 15:29
# @describe : 


import multiprocessing


def test(q):        # 把进程Queue对象传入传入子进程
    q.put('lws')

if __name__ == '__main__':
    q = multiprocessing.Queue()     # 实例化进程Queue对象
    p = multiprocessing.Process(target=test, args=(q,))     # 创建多进程
    p.start()
    print q.get()       # 读取Queue数据
