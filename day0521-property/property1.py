# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/5/21 20:36
# @describe : 私有属性的访问及property使用


class Test(object):
    def __init__(self):
        self.__num = 0

    def SetNum(self, newnum):
        self.__num = newnum

    def GetNum(self):
        return self.__num

    num = property(GetNum, SetNum)   # 使用property方法函数名get在前set在后

t = Test()
t.num = 100
print t.num






