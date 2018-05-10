# -*- coding: utf-8 -*-

# @Author : lws
# @Time   : 2018/5/10 22:58

from threading import Thread, Lock

num = 0


def test1():
    global num
    mutex.acquire()
    for i in range(1000000):
        num += 1
    mutex.release()
    print "test1:%d" % num


def test2():
    global num
    mutex.acquire()
    for i in range(1000000):
        num += 1
    mutex.release()
    print "test2:%d" % num

if __name__ == "__main__":
    mutex = Lock()
    t1 = Thread(target=test1)
    t1.start()
    t2 = Thread(target=test2)
    t2.start()
    print "num:%d" % num




