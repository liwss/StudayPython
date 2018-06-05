# coding=utf-8

from socket import *
from time import ctime


host = ''
port = 7777
bufsize = 1024
ADDR = (host, port)

s = socket(AF_INET, SOCK_DGRAM)
s.bind(ADDR)

while True:
    print 'waiting for message ......'
    date, addr = s.recvfrom(bufsize)
    s.sendto('[%s] %s' % (ctime(), date),addr)
    print 'recved from add returned to :',addr

s.close()
