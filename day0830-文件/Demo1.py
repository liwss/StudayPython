# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/8/30 10:34
# @describe : 

import time

# f = open("test.txt", "r")
# for index, data in enumerate(f.readlines()):
#     # readline()和readlines()把文件内容读到内存中，适合小文件，读大文件可能导致内存不足
#     print (index, '-----------'+data.strip())
#     time.sleep(0.5)

# f = open("test.txt", "r")   # 可以读取大文件且效率高，f迭代器方式取出，每读取一行就会覆盖之前的，所以不会内存不足
# for line in f:
#     time.sleep(1)
#     print (line.strip())
#     # print (f.encoding)   # 打印文件编码
#     print (f.name)         # 打印文件名称
# f.close()                  # 关闭文件句柄，使用with open() as:可以不用手动关闭句柄

with open("test.txt", "r") as f:
    a = f.readlines()
    b = f.readline()
    print (a)
    print (b)



