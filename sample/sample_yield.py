"""
https://blog.csdn.net/mieleizhi0522/article/details/82142856

yield from 是在Python3.3才出现的语法。
yield from 后面需要加的是可迭代对象，它可以是普通的可迭代对象，也可以是迭代器，甚至是生成器。
"""

def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:", res)


def foo2(num):
    print("starting...")
    while num < 10:
        num += 1
        yield num

def test1():
    g = foo()
    # <generator object foo at 0x0000000003172A50>
    print(g)

    # @1 首次 next foo()，打印"starting..."，运行到 " res = yield 4"，返回 4，挂起
    print(next(g))
    # @2 打印 20 个星号
    print("*"*20)
    # @3 又 next foo()，从挂起的位置接着运行，打印“res: None”。又运行到 "res = yield 4"，返回 4，挂起
    print(next(g))
    # 关闭生成器
    g.close()
    print("\n")

def test2():
    f = foo2(0)
    for n in f:
        print(n)
    f.close()

def gen_yield(*args, **kw):
    for item in args:
        for i in item:
            yield i

def gen_yield_from(*args, **kw):
    for item in args:
        # yield from 后面加上可迭代对象
        yield from item

def test3():
    astr='ABC'
    alist=[1,2,3]
    adict={"name":"wangbm","age":18}
    agen=(i for i in range(4,8))

    new_list1=gen_yield(astr, alist, adict, agen)
    # <generator object gen at 0x0000000003162B30>
    print(new_list1)
    print(list(new_list1))
    
    print()
    
    new_list2=gen_yield(astr, alist, adict, agen)
    # <generator object gen at 0x0000000003162B30>
    print(new_list2)
    print(list(new_list2))
    
    

if __name__ == '__main__':
    test3()

'''
def echo(value=None):
    print("Execution starts when 'next()' is called for the first time.")
    try:
        while True:
            try:
                value = yield value
            except Exception as e:
                value = e
    finally:
        print("Don't forget to clean up when 'close()' is called.")
generator = echo(666)
print(next(generator))
print(next(generator))
print(next(generator))
# print(generator.send(2))
# generator.throw(TypeError, "spam")
generator.close()
'''
