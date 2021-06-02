# coding:utf-8
"""

获取文件名：
filename = 'C:\\Test\\v2idemo.text'.split(os.sep)[-1].split('.')[0]


"""

import xlrd
from os import path, sep
import os

def test2():
    current_dir = path.dirname(path.abspath(__file__))
    file_name = f'{current_dir}{sep}sample.xls'
    print('文件全路径：', file_name)

    # 打开Excel文件读取数据
    book = xlrd.open_workbook(file_name)

    sheet_count = book.nsheets
    print("表格数量：", sheet_count)

    # 获取所有sheet名称
    sheet_names = book.sheet_names()
    for sheet_name in sheet_names:
        print(sheet_name)

    print()

    for index, sheet_name in enumerate(sheet_names):
        print(f'索引：{index} - 表格名称：{sheet_name}')
        sheet = book.sheet_by_index(index)
        print(f'表格名称：{sheet.name} 行数：{sheet.nrows} 列数：{sheet.ncols}')
        for row in range(0, sheet.nrows):
            for col in range(0, sheet.ncols):
                # ord('A') = 65; chr(65) = 'A'
                print(f'{chr(col+65)}{row+1} - {sheet.cell_value(row, col)}')
        print()
        for rx in range(sheet.nrows):
            print(sheet.row(rx))
        print()

def get_filename(path):
    if path:
        return path.split(os.sep)[-1].split('.')[0]
    else:
        return None

def test3():
    print(get_filename('C:\\Test\\v2idemo.text'))
    print(get_filename('C:\\Test\\v2idemo'))
    print(get_filename('v2idemo.text'))
    print(get_filename('v2idemo'))
    print(get_filename(''))


if __name__ == '__main__':
    test3()
