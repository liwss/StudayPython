# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/3 15:28
# @describe : 字符编码与转换（py2）

import sys

print (sys.getdefaultencoding())   # 打印系统默认编码

# py2  字符转码需要先把编码解码成unicode编码，再转码成其它编码
# py2 默认字符编码为ascii码，utf-8编码是Unicode码的扩展集

# s = "你好"
s = u"你好"  # 指定字符编码为Unicode
print (s, type(s))
# s_2_gbk = s.decode("utf-8").encode("gbk")  # 把utf-8编码的s解码成unicode,再转码成gbk格式
s_2_gbk = s.encode("gbk")  # 把Unicode编码转成gbk
print (s_2_gbk)
