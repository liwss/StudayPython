# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/10 15:04
# @describe : 解析xml字符串

import xml.etree.ElementTree as ET

xmlstr = """
<root>
    <person>
        <name>liws</name>
        <age>20</age>
    </person>
    <person>
        <name>820</name>
        <age>15</age>
    </person>
</root>
"""
tree = ET.fromstring(xmlstr)
print tree.tag      # 获取根节点

for node in tree.iter('age'):  # 遍历查询xml中某个节点
    print node.text

# name = tree.getiterator('name')  # 获得指定节点
# for i in name:
#     print i.text

name = tree.findall('person')
print name
for node in name:
    for i in node:
        print i.text




