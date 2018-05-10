# -*- coding: utf-8 -*-

# @Author : lws
# @Time   : 2018/5/10 18:13

import time
from multiprocessing import Queue, Process


def WriteQ(q):
    for value in range(5):
        print "put %d in Queue ..." % value
        q.put(value)
        time.sleep(0.5)


def ReadQ(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print "Get %d from Queue" % value
            time.sleep(0.5)
        else:
            break
if __name__ == "__main__":
    q = Queue()
    pw = Process(target=WriteQ, args=(q,))
    pr = Process(target=ReadQ, args=(q,))
    pw.start()
    pw.join()
    pr.start()
    pr.join()


