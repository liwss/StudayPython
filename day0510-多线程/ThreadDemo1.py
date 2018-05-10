# -*- coding: utf-8 -*-

# @Author : lws
# @Time   : 2018/5/10 20:27


from threading import Thread
import time


def test(n):
    print "我是子线程%d执行的" % n
    time.sleep(1)
    print "------------------"

for i in range(5):
    t = Thread(target=test, args=(i,))
    t.start()





