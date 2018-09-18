# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/18 11:51
# @describe : 继承threading类创建线程

import threading


class MyThread(threading.Thread):           # 创建新类继承thread类
    def __init__(self, num):
        # threading.Thread.__init__(self)   # 调用父类构造方法初始化
        super(MyThread, self).__init__()
        self.num = num

    def run(self):                          # 重写run方法
        print "threading %s" % self.num

if __name__ == '__main__':
    t1 = MyThread(1)        # 实例化MyThread类
    t2 = MyThread(2)
    t1.start()              # 启动线程
    t2.start()