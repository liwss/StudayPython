# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/27 15:06
# @describe : 

import multiprocessing
import time
import os


def test(num):
    time.sleep(1)
    print "processing %s" % num
    return num


def work(num):  # 回调函数的入参是多进程任务的返回值，且回调函数是由主进程调用
    print "----callback----%s----%s---" % (num, os.getpid())

if __name__ == '__main__':
    print "main processing %s ..." % os.getpid()
    p = multiprocessing.Pool(3)     # 创建进程池,最多同时存在3个
    for i in range(10):
        # p.apply(test, (i,))       # 阻塞方式启动，一个进程结束，释放回进程池，下一个进程开始执行
        p.apply_async(test, (i,), callback=work)   # 非阻塞方式启动，并行执行
    p.close()
    p.join()        # 主程序等待子进程结束，先close再join
    print "-----------"
