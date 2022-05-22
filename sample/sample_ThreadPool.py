# coding: utf-8

from concurrent.futures import ThreadPoolExecutor
import os
import threading
from time import sleep


def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + '  ' + str(i))
        sleep(0.5)
        my_sum += i
    return my_sum


def test():
    pool = ThreadPoolExecutor(max_workers=2)
    pool.submit(action, 5)
    # print(future1.done())
    # print(future1.result())
    print('aaabbb')


if __name__ == '__main__':
    pass
