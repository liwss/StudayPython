# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/18 10:45
# @describe : 


import paramiko


transport = paramiko.Transport(('172.21.10.136', 22))
transport.connect(username='appsgw', password='appsgw')

sftp = paramiko.SFTPClient.from_transport(transport)

# 上传本地文件上传到服务器（参数1:本地文件 2：指定上传到服务器的文件目录及文件名）
sftp.put('/crmpdpp/sgwadm/work/ssh_client.py', '/crmpdpp/sgwadm/work/liws/ssh_client.py')

# 将远端文件下载到本地（参数1：远端服务器文件 2：指定下载到本地的路径及文件名）
# sftp.get('/crmpdpp/sgwadm/work/liws/ssh_client.py', '/crmpdpp/sgwadm/work/ssh_client.py')

transport.close()
