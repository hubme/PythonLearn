# coding: utf-8

""" 
1. 默认级别是 WARNING
2. https://docs.python.org/zh-cn/3/howto/logging.html
"""

import logging
from os import path


def method1():
    logging.warning('Watch out!')  # will print a message to the console
    logging.info('I told you so')  # will not print anything


def method2():
    cur_dir = path.dirname(path.abspath(__file__))
    log_path = path.join(cur_dir, 'example.log')
    print('log_path', log_path)

    logging.basicConfig(filename=log_path, encoding='utf-8', level=logging.DEBUG)

    # logging.basicConfig(filename=log_path, level=logging.DEBUG,
    # filemode = 'w', format='%(levelname)s:%(asctime)s:%(message)s', datefmt='%Y-%d-%m %H:%M:%S')
    
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')
    logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
    
    
if __name__ == '__main__':
    method2()