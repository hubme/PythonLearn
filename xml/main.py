# coding: utf-8

# from os import path
from os import path, sep
from io import StringIO, BytesIO
from lxml import etree

def read_xml():
    """ 
    https://lxml.de/parsing.html
    """
    # current_dir = path
    current_dir = path.dirname(path.abspath(__file__))
    xml_file_path = f'{current_dir}{sep}resources{sep}IM_zh-cn_small.xml'
    print(f'xml 文件路径：{xml_file_path}')

    tree = etree.parse(xml_file_path)
    # tree = etree.parse('c:/Python/PythonLearn/xml/resources/IM_zh-cn_small.xml')

    print(etree.tostring(tree.getroot()))

if __name__ == '__main__':
    read_xml()