# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/13 11:15
# @describe :


class Test(object):
    def __new__(cls, *args, **kwargs):
        print ("---new---")
        return object.__new__(cls)

    def __init__(self, name):
        self.name = name
        print ("---init---")

a = Test('lws')
