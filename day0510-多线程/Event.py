# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/18 17:57
# @describe : 

import threading
import time

event = threading.Event()


def test(name):
    print "threading %s is coming ...." % name
    event.wait()
    time.sleep(2)
    print "threading %s ......" % name

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=test, args=(i,))
        t.start()

    event.set()