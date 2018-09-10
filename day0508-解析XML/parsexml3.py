# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/10 15:04
# @describe : 解析xml字符串

import xml.etree.ElementTree as ET

xmlstr = """
<root>
    <name>liws</name>
</root>
"""

root = ET.fromstring(xmlstr)
print root.tag

for node in root.iter('name'):  # 遍历查询xml中某个节点
    print node.text

name = root.getiterator('name')
for i in name:
    print i.text


