# https://blog.csdn.net/mieleizhi0522/article/details/82142856

def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:", res)


g = foo()

# @1 首次 next foo()，打印"starting..."，运行到 " res = yield 4"，返回 4，挂起
print(next(g))
# @2 打印 20 个星号
print("*"*20)
# @3 又 next foo()，从挂起的位置接着运行，打印“res: None”。又运行到 "res = yield 4"，返回 4，挂起
print(next(g))
# 关闭生成器
g.close()
print("\n")


def foo2(num):
    print("starting...")
    while num < 10:
        num += 1
        yield num


f = foo2(0)
for n in f:
    print(n)
f.close()


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
