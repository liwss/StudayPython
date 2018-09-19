# -*- coding: utf-8 -*-

# @Author : lws
# @Time   : 2018/5/9 22:24


from multiprocessing import Process
import time


def test(name):
    for i in range(3):
        print "hello %s" % name
        time.sleep(1)

if __name__ == "__main__":
    p = Process(target=test, args=("liws",))
    p.start()
    p.join(1)      # 是否等待进程实例结束，参数为等待timeout，默认一直等待
    print "_____end_____"



