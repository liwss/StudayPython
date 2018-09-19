# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/19 16:39
# @describe : Manager用于多进程间共享变量

from multiprocessing import Process, Manager
import os


def f(d, l):
    d[os.getpid()] = os.getpid()
    l.append(os.getpid())
    print(l)

if __name__ == '__main__':
    # with Manager() as mgr:    # 同下创建方式等价
    mgr = Manager()
    d = mgr.dict()          # {} 生成一个字典，可在多个进程间共享和传递
    l = mgr.list(range(5))  # 生成一个列表，可在多个进程间共享和传递
    p_list = []
    for i in range(10):
        p = Process(target=f, args=(d, l))
        p.start()
        p_list.append(p)
    for res in p_list:  # 等待结果
        res.join()

    print(d)
    print(l)
