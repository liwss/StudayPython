# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/18 10:18
# @describe : 

import paramiko

transport = paramiko.Transport(('172.21.10.136', 22))
transport.connect(username='appsgw', password='appsgw')

ssh = paramiko.SSHClient()
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('ps -ef|grep nginx|grep -v grep|wc -l')
print stdout.read()
transport.close()
