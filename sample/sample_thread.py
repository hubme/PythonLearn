# coding: utf-8

import threading
from time import sleep


def task(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + '  ' + str(i))
        sleep(0.5)
        my_sum += i
    return my_sum


def test_thread():

    thread = threading.Thread(target=task, args=(5, ))
    thread.start()


if __name__ == '__main__':
    print(threading.current_thread().name)
    # test_thread()
    thread = threading.Thread(target={print('hhh')}, args=())
    thread.start()
