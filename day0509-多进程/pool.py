# -*- coding: utf-8 -*-

# @Author : lws
# @Time   : 2018/5/10 11:01

import os
import time
from multiprocessing import Pool


def worker(msg):
    print "%s begin，processing：%s" % (msg, os.getgid())
    time.sleep(0.1)


if __name__ == "__main__":
    p = Pool(3)
    for i in range(10):
        p.apply_async(worker, (i,))

    print "____start____"
    p.close()
    p.join()
    print "_____end_____"

