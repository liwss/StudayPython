# coding=utf-8

import os

ret = os.fork()

if ret == 0:
	print "我是子进程：%d ,我的父进程是:%d" %(os.getpid(), os.getppid())
else:
	print "我是父进程：%d" %(os.getpid())    
