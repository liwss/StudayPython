# -*- coding: utf-8 -*-

# @Author : lws
# @Time   : 2018/5/10 11:01

import os
import time
from multiprocessing import Pool


def worker(msg):
    print "%d begin，processing：%d" % (msg, os.getpid())
    time.sleep(1)


if __name__ == "__main__":
    p = Pool(3)
    for i in range(10):
        # p.apply_async(worker, (i,))  # apply_async非阻塞式，并行执行，
        p.apply(worker, (i,)) # apply(func[, args[, kwds]])：使用阻塞方式调用func

    print "____start____%d" % os.getpid()
    p.close()
    p.join()
    print "_____end_____"

