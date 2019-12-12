# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2019/9/29 11:01
# @describe : 


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
import time

Base = declarative_base()


class EaiInformation(Base):
    __tablename__ = 'EAI_INFORMATION'
    ip = Column('IP', String, primary_key=True)
    port = Column('PORT', String)
    appid = Column('APPID', String)
    transcode = Column('TRANSCODE', String)
    url = Column('REMOUTE_URL', String)


t = time.time()

engine = create_engine('oracle://dbinter:Dbinter123.com@172.18.238.229:1632/hkthradb', echo=True)
db_session = sessionmaker(bind=engine)
session = db_session()
stu = session.query(EaiInformation).filter(EaiInformation.port == '55555').all()

for s in stu:
    print s.ip, s.port, s.appid, s.transcode, s.url
t1 = time.time()-t
print t1


