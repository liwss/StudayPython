# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/11/16 9:37
# @describe : 


def test1(func):
    print '-----------test1-------------'

    def test2():
        print '------------test2--------------'
        return func()
    return test2


@test1   # test3 = test1(test3)
def test3():
    print '----------test3--------------'


test3()
