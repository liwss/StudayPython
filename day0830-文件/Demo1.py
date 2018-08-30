# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/8/30 10:34
# @describe : 

import time

f = open("test.txt", "r")
for index, data in enumerate(f.readlines()):
    print (index, '-----------'+data.strip())
    time.sleep(0.5)







