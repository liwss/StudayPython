# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/12/4 15:05
# @describe : 斐波那契数列


# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print b
#         a, b = b, a+b
#         n = n + 1

# fab(5)

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


for b in fab(5):
    print b