# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/3 16:04
# @describe : 字符编码与转码py3


import sys

print(sys.getdefaultencoding())  # py3默认系统编码为utf-8

s = "你好"
print(s)
s1 = s.encode("gbk")
print(s1, type(s1))
s2 = s1.decode("gbk").encode("utf-8")
print(s2, type(s2))
s3 = s2
print(s3.decode(), type(s3.decode()))
