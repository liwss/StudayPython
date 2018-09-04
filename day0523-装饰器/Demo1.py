# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/4 8:47
# @describe : 常用高阶函数

L = [1, 2, 3, 4, 5]
print (map(lambda x: x**2, L))

print (reduce(lambda x, y: x+y, map(lambda x: x**2, L)))

print (filter(lambda x: x % 2 != 0, map(lambda x: x**2, L)))

L1 = [3, 4, 2, 1, 5]
# L1.sort()
# print (L1)  # sort()原列表基础上排序，不会得到新列表，改变原列表

print (sorted(L1))  # sorted()得到新的列表，不改变原列表
print (L1)

L2 = [('a', 3), ('b', 2), ('c', 1)]
print (sorted(L2, cmp=lambda x, y: cmp(x[1], y[1])))
print (sorted(L2, key=lambda x: x[0]))
