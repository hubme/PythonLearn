from functools import wraps


def somefunc_decorator(func):
    """ 包装原有方法的装饰器方法。 """
    @wraps(func)
    def wrap_func(*args, **kwargs):
        """ wrap_func doc."""
        print(f"before exec {func.__name__}")
        func(*args, **kwargs)
        print(f"after exec {func.__name__}")

    return wrap_func


def somefunc():
    """ somefunc doc. """
    print("print somefunc.")


# 注解方法需要写在被注解方法的前面。NameError: name 'somefunc_decorator' is not defined
@somefunc_decorator
def somefunc2():
    """ somefunc2 doc. """
    print("print somefunc2.")


def test1():
    somefunc()
    print()

    # somefunc_decorator(somefunc)()
    f = somefunc_decorator(somefunc)
    f()


def test2():
    somefunc2()


def test3():
    # 不加 @wraps 输出：The name of somefunc2: wrap_func
    # 加 @wraps 输出：The name of somefunc2: somefunc2
    print(f'The name of somefunc2: {somefunc2.__name__}')


if __name__ == "__main__":
    test1()
    # test2()
    # test3()
