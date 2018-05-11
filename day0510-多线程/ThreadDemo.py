# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/5/11 9:06
# @describe : 多线程，局部变量非共享,互不影响

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, num, SleepTime):
        threading.Thread.__init__(self)
        self.num = num
        self.SleepTime = SleepTime

    def run(self):
        self.num += 1
        time.sleep(self.SleepTime)
        print "线程:%s, num=%d" % (self.name, self.num)

if __name__ == "__main__":
    t1 = MyThread(100, 1)
    t1.start()
    t2 = MyThread(200, 1)
    t2.start()





