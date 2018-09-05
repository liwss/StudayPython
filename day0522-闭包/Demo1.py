# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/5 10:03
# @describe : 闭包


def test():
    x = 1

    def test1():
        return x+1
    return test1


print test()()
