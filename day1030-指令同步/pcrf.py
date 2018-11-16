# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/10/30 9:50
# @describe : 爱立信PCRF割接华为指令同步

from multiprocessing import Pool, Queue
import requests
import time


def readfile():
    with open('pcrf.txt', 'r') as f:
        for line in f:
            time.sleep(0.5)
            # print line
            q.put(line)


def callserv():
    url = ''
    headers = {'content-type': 'application/json'}
    recvmsg = requests.post(url, data=inputmsg, headers=headers).text.strip()

if __name__ == '__main__':
    q = Queue()
    p = Pool(5)

