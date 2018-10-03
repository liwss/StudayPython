# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/27 17:16
# @describe : 

from greenlet import greenlet


def test1():
    print '1...'
    g2.switch()
    print '3...'
    g2.switch()


def test2():
    print '2...'
    g1.switch()
    print '4...'

if __name__ == '__main__':
    g1 = greenlet(test1)    # 启动一个协程并加入任务
    g2 = greenlet(test2)
    g1.switch()             # 切换到任务g1

