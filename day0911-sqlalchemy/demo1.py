# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2019/9/11 15:32
# @describe : 

from sqlalchemy import create_engine

engine = create_engine('mysql://lws:lws820@39.107.88.145:3306/test?charset=utf8', echo=True)
