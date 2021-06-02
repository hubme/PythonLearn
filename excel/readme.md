# Python Excel 表格处理

[Working with Excel Files in Python](https://www.python-excel.org/)

**Excel xls 和 xlsx 区别：**

1. 文件格式不同。xls 是一个特有的二进制格式，其核心结bai构是复合文档类型的结构，
而 xlsx 的核心结构是 XML 类型的结构，采用的是基于 XML 的压缩方式，使其占用的空间更小。xlsx 中最后一个 x 的意义就在于此。
2. 版本不同。xls是excel2003及以前版本生成的文件格式，而xlsx是excel2007及以后版本生成的文件格式。
3. 兼容性不同。xlsx格式是向下兼容的，可兼容xls格式。

## xlrd

> xlrd is a library for reading data and formatting information from Excel files in the historical .xls format.

`This library will no longer read anything other than .xls files.`

pip3 install xlrd（安装 python3 版本）

- [官网](https://pypi.org/project/xlrd/)
- [pip 下载地址](https://pypi.org/project/xlrd/)

## openpyxl

- [官网](https://openpyxl.readthedocs.io)