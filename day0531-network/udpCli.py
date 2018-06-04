# coding=utf-8


from socket import *
from time import ctime

host = '127.0.0.1'
port = 7777
bufsize = 1024
ADDR = (host, port)

s = socket(AF_INET, SOCK_DGRAM)

while True:
    date = raw_input('>>')
    if not date:
        break
    s.sendto(date, ADDR)
    date, addr = s.recvfrom(bufsize)
    if not date:
        break
    print date
s.close()

