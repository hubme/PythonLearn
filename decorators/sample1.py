"""
装饰器使用示例。
"""

import time
from functools import wraps


def somefunc_new(func):
    """ 包装原来的方法 """
    # 使用标准库中提供的一个 wraps 装饰器，将被装饰函数的信息复制给 wrapper 函数
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@somefunc_new
def somefunc(sleep):
    '''
    这是文档字符串
    somefunc
    '''
    time.sleep(sleep)
    return sleep


if __name__ == "__main__":
    somefunc(2)

    # somefunc.__name__ 等价于 somefunc_new(somefunc).__name__，所以返回值为 wrapper
    print(somefunc.__name__)
    print(somefunc.__doc__)
