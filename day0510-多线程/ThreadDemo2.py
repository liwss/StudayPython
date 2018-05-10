# -*- coding: utf-8 -*-

# @Author : lws
# @Time   : 2018/5/10 21:01


from threading import Thread
import time


class MyThread(Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "我是线程:"+self.name+'@'+ str(i)+'\n'
            print msg


def test():
    for i in range(3):
        t = MyThread()
        t.start()

if __name__ == "__main__":
    test()

