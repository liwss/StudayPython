# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/5/21 22:46
# @describe : yield创建生成器


def Test():
    i = 0
    while True:
        yield i   # 每次执行都会卡在yeild处
        i+=1


t = Test()
a = t.next()
print a
b = t.next()
print b
c = t.next()
print c










