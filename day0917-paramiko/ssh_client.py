# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/17 18:00
# @describe : 


import paramiko

ssh = paramiko.SSHClient()      # 实例ssh客户端对象
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在Know_hosts文件中的主机
ssh.connect(hostname='172.21.10.136', port=22, username='appsgw', password='appsgw')
stdin, stdout, stderr = ssh.exec_command('ps -ef|grep nginx|grep -v grep|wc -l')  # 执行命令
print stdin             # 标准输入流
print stdout.read()     # 标准输出，返回结果
print stderr.read()     # 标准出错，错误结果
ssh.close()             # 关闭连接
