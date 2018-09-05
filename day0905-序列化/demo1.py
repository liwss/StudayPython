# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/5 17:23
# @describe :

import pickle
import json


def test():
    print ("in the test")


info = {"a":"1", "b":"2", "c":"3", "func":test}

with open("test.txt", 'w') as f:
    f.write(pickle.dumps(info))
