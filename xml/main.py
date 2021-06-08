# coding: utf-8

# from os import path
from os import path, sep
from io import StringIO, BytesIO
from lxml import etree
from pprint import pprint

def read_xml():
    """
    https://lxml.de/tutorial.html
    https://lxml.de/parsing.html
    https://developer.android.com/guide/topics/resources/string-resource
    """
    current_dir = path.dirname(path.abspath(__file__))
    xml_file_path = f'{current_dir}{sep}resources{sep}strings.xml'
    print(f'xml 文件路径：{xml_file_path}')

    # remove_comments - discard comments
    parser = etree.XMLParser(remove_comments=True, strip_cdata=False)
    tree = etree.parse(xml_file_path, parser)

    root = tree.getroot()
    print(f'根节点：{root.tag}')
    # pprint(etree.tostring(root, pretty_print=True).decode('utf-8'))
    for e in root:
        print(e.tag, e.get('name'), e.text, '子元素个数：', len(e))
        # 有子元素
        """ if len(e) > 0:
            for ele in e:
                print(ele.tag, ele.text) """

    # print(root[1].getprevious().get('name')) # 获取当前元素的前一个元素
    # print(root[1].getnext().get('name')) # 获取当前元素的后一个元素

def write_xml():
    root = etree.Element('html', version='5.0')
    etree.SubElement(root, 'head')
    etree.SubElement(root, 'title', bgColor='red', fondsize='22')
    etree.SubElement(root, 'body', fontsize='15')

    # root.set("hello", "Huhu")
    aaa_ele = etree.Element('aaa', interesting="totally")
    aaa_ele.text = 'aaa value'

    # 修改或添加属性
    aaa_ele.set('interesting', 'totally-2')
    aaa_ele.set('name', 'hahah')
    root.append(aaa_ele)

    # 直接操作属性字典
    # attributes = aaa_ele.attrib
    # print(attributes["interesting"])

    # 遍历元素中的所有属性
    for name, value in sorted(aaa_ele.items()):
        print(f'{name} = {value}')

    root.insert(0, etree.Element("child0"))

    result = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='utf-8').decode('utf-8')
    print(result)
    
def aaa():
    with etree.xmlfile('somefile.xml', encoding='utf-8', close=True) as xf:
        xf.write_declaration()
        # xf.write_doctype('<!DOCTYPE root SYSTEM "some.dtd">')

        # generate an element (the root element)
        with xf.element('root'):
            # write a complete Element into the open root element
            test_ele = etree.Element('test')
            test_ele.text = 'text value'
            test_ele['name'] = 'key'
            xf.write(test_ele)

            # generate and write more Elements, e.g. through iterparse
            # for element in generate_some_elements():
                # serialise generated elements into the XML file
                # xf.write(element)

            # or write multiple Elements or strings at once
            xf.write(etree.Element('start'), "text", etree.Element('end'))

def testCData():
    """
    https://lxml.de/api.html#cdata
    """
    parser = etree.XMLParser(strip_cdata=False)
    root = etree.XML('<root><![CDATA[test]]></root>', parser)
    print(root.text)

if __name__ == '__main__':
    write_xml()
    