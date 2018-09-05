# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/5 17:25
# @describe :

import pickle
import json


def test():
    print ("in the test1")

with open("test.txt", "r") as f:
    data = pickle.loads(f.read())


print data['func']()
