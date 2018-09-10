# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/10 10:20
# @describe : 解析xml

import xml.etree.ElementTree as ET

tree = ET.parse("xml")  # 加载要解析的xml文件
root = tree.getroot()   # 获取xml根节点
print (root)
print (root.tag)        # 打印根节点

for child in root:      # 遍历根节点下的一级子节点
    print (child.tag, child.attrib, child.text)  # 节点名、节点属性、节点内容
    for i in child:     # 遍历二级子节点
        print (i.tag, i.attrib, i.text)

for node in root.iter('CUR_SCORE'):  # 遍历查询xml中某个节点
    print node.text

# 修改xml节点值及属性
for node in root.iter("RETURN_CODE"):
     node.text = '0000'             # 需要修改的节点值
     node.set('type', 'string')     # 修改属性值
     node.set('test', 'test')       # 新增属性及赋值
tree.write('xml')                   # 写入文件

# 删除xml节点
for node in root.findall("RETURN_MSG"):  # 遍历查询需要删除的节点
    root.remove(node)               # 删除节点
tree.write('xml')                   # 写入文件