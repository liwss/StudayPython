# -*- coding: utf-8 -*-

# @Author : lws
# @Time   : 2018/5/10 18:30

from multiprocessing import Manager, Pool
import os


def reader(q):
    print "reader启动(%s)" % os.getpid()
    for i in range(q.qsize()):
        print "reader从Queue获取到消息：%s" % q.get(True)


def writer(q):
    print "writer启动(%d)" % os.getpid()
    for i in range(4):
        q.put(i)

if __name__ == "__main__":
    print "(%d) start" % os.getpid()
    q = Manager().Queue()  # 使用Manager中的Queue来初始化
    po = Pool(4)
    # 使用阻塞模式创建进程，这样就不需要在reader中使用死循环了，可以让writer完全执行完成后，再用reader去读取
    po.apply(writer, (q,))
    po.apply(reader, (q,))
    po.close()
    po.join()
    print "(%d) End" % os.getpid()





