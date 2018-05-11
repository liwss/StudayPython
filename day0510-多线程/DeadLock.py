# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/5/11 9:29
# @describe : 多线程死锁的Demo

from threading import Thread, Lock
import time


def test1():
    if mutex1.acquire():
        print "test1启动"
        time.sleep(1)
        if mutex2.acquire():
            print "test2停止"
        mutex1.release()


def test2():
    if mutex2.acquire():
        print "test2启动"
        time.sleep(1)
        if mutex1.acquire():
            print "test2停止"
        mutex1.release()

if __name__ == "__main__":
    mutex1 = Lock()
    mutex2 = Lock()
    t1 = Thread(target=test1)
    t2 = Thread(target=test2)
    t1.start()
    t2.start()







