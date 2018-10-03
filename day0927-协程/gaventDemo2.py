# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/27 17:37
# @describe : 


import gevent


def test1():
    print '1...'
    gevent.sleep(1)
    print '3....'


def test2():
    print '2....'
    gevent.sleep(1)
    print '4....'


def test3():
    print '5....'
    gevent.sleep(2)
    print '6....'

if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(test1),
        gevent.spawn(test2),
        gevent.spawn(test3)
    ])
