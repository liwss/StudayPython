# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2019/1/28 16:27
# @describe : 从旧文件中找出在新文件中不存在的数据

fo = open("old.txt", "r", encoding='utf-8')
fn = open("new.txt", "r", encoding='utf-8')
olist = []
nlist = []
for data in fo.readlines():
    olist.append(data.strip())

for data in fn.readlines():
    nlist.append(data.strip())

for data in olist:
    if data in nlist:
        print(data)