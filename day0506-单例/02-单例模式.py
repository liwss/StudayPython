# coding=utf-8

class A(object):

    __instance = None   # 定义类属性
    __flag = False     

    def __new__(cls, *argv, **kargvs):
        """单例模式"""
        if cls. __instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance
    
    def __init__(self, name):
        if A.__flag == False:
            self.name = name
            A.__flag = True


a = A("lws")
print (a.name)
b = A("zh")
print (b.name)
print (b.name)
print (b.name)
print (a.name)
