# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/7/10 14:48
# @describe : 

# json转换xml
import xmltodict
import json


def python_conver_xml_to_json():
    """
    demo Python conversion between xml and json
    :return:
    """
    xml = """
    <data>
        <country name="Liechtenstein">
            <rank updated="yes">2</rank>
            <year>2023</year>
            <gdppc>141100</gdppc>
            <neighbor direction="E" name="Austria" />
            <neighbor direction="W" name="Switzerland" />
        </country>
        <country name="Singapore">
            <rank updated="yes">5</rank>
            <year>2026</year>
            <gdppc>59900</gdppc>
            <neighbor direction="N" name="Malaysia" />
        </country>
        <country name="Panama">
            <rank updated="yes">69</rank>
            <year>2026</year>
            <gdppc>13600</gdppc>
            <neighbor direction="W" name="Costa Rica" />
            <neighbor direction="E" name="Colombia" />
        </country>
    </data>
    """
    dic = xmltodict.parse(xml)
    # json_str = json.dumps(dic)  # 默认没有进行格式化
    json_str = json.dumps(dic, indent=1)  # 默认没有进行格式化
    print(json_str)


def python_conver_json_to_xml():
    """
    demo Python conversion between xml and json
    :return:
    """
    dic = {
        'page': {
            'title': 'King Crimson',
            'ns': 0,
            'revision': {
                'id': 547909091,
            }
        }
    }
    xml = xmltodict.unparse(dic)
    print(xml)


if __name__ == '__main__':
    python_conver_xml_to_json()
    python_conver_json_to_xml()
