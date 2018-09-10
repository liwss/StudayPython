# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/9/10 11:49
# @describe : 创建xml文件

import xml.etree.ElementTree as ET

root = ET.Element('root')   # 创建根节点root
person = ET.SubElement(root, 'person')  # 创建子节点person
name = ET.SubElement(person, 'name', attrib={"type": "String"})     # 创建二级子节点name，并添加属性
age = ET.SubElement(person, 'age', attrib={"type": "String"})       # 创建二级子节点age，并添加属性
name.text = 'liws'  # 给节点赋值
age.text = '25'
et = ET.ElementTree(root)   # 生成文档对象
et.write("test.xml", encoding='utf-8', xml_declaration=True)    # 写入文件，指定编码格式和xml头信息

