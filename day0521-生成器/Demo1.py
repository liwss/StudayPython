# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/5 14:48
# @describe : 斐波那契


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n+1

f = fib(5)
print (f.next())
print (f.next())
print (f.next())
print (f.next())
print (f.next())


