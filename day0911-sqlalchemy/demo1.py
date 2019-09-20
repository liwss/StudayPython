# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2019/9/11 15:32
# @describe : 创建表 create table

from sqlalchemy import create_engine, MetaData, Column, Table, String, Integer

engine = create_engine('mysql://lws:lws820@39.107.88.145:3306/test01?charset=utf8', echo=True)

# MetaData类主要用于保存表结构,连接字符串等数据,是一个多表共享的对象
metadata = MetaData(engine)  # 绑定一个数据源的metadata

student = Table('student', metadata,
                Column('id', Integer, primary_key=True),
                Column('name', String(50),),
                Column('age', Integer,),
                Column('address', String(10),),
)

metadata.create_all(engine)  # 创建表,会先判断表是否存在
