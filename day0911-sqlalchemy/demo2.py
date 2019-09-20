# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2019/9/12 11:12
# @describe : 插入数据 insert

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://lws:lws820@39.107.88.145:3306/test01?charset=utf8', echo=True)
db_session = sessionmaker(bind=engine)
session = db_session()
Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    address = Column(String(100))


stu1 = Student(id=1001, name='tom', age=23, address='beijing')
stu2 = Student(id=1002, name='Ame', age=33, address='shanghai')
stu3 = Student(id=1003, name='jack', age=26, address='xian')
stu4 = Student(id=1004, name='jean', age=29, address='shenzhen')


session.add_all([stu1, stu2, stu3, stu4])
# session.add(stu4)
session.commit()
session.close()