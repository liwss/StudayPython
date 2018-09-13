# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/13 9:55
# @describe : __call__()方法是对像()或者类名()()时自动调用
#             __dict__()方法是如果用类名调用就是打印类所有属性包括实例属性
#                            如果用对象调用就是打印实例属性


class Test(object):
    def __init__(self, name):
        self.name = name
        print ("-----------------")

    def __call__(self, *args, **kwargs):   # __call__()方法是对像()或者类名()()时自动调用
        print ("++++++++++++++++++")

    def __str__(self):
        return '<obj:%s>' % self.name


a = Test('lws')
a()   # 等价于Test()()   调用__call__()
print type(Test)
