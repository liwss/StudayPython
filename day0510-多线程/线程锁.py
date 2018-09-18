# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/18 17:27
# @describe : 

import threading
import time


def test(name):
    lock.acquire()  # 加锁
    time.sleep(1)
    print "threding %s ..." % name
    lock.release()  # 释放锁


if __name__ == '__main__':
    lock = threading.Lock()     # 实例化锁对象
    for i in range(3):
        t = threading.Thread(target=test, args=(i,))  # 创建线程
        t.start()