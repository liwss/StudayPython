# coding=utf-8
# /usr/bin/python3

date = ['lws', '25', '31313213@qq.com', '43242423@qq.com']
name, age, _, _ = date
print ("name=%s,age=%s\n"% (name, age))


name, age, *email = date
print ("name=%s,age=%s,email=%s\n"% (name, age,email))
