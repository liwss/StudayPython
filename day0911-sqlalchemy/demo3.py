# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2019/9/12 11:33
# @describe : 查询数据 select

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    address = Column(String(100))


engine = create_engine('mysql://lws:lws820@39.107.88.145:3306/test01?charset=utf8', echo=True)
db_session = sessionmaker(bind=engine)
session = db_session()

stu = session.query(Student).filter(func.substr(Student.age, 2, 1) == 3).all()

for s in stu:
    print s.name