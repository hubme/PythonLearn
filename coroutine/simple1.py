import asyncio

"""
https://docs.python.org/zh-cn/3/library/asyncio-task.html

协程中的状态:

Pending：创建future，还未执行
Running：事件循环正在调用执行任务
Done：任务执行完毕
Cancelled：Task被取消后的状态 
"""

async def hello(name):
    await asyncio.sleep(2)
    print('hello', name)
    
def test1():
    
    # 定义协程对象
    coroutine = hello('world!')

    # 定义事件循环对象容器
    loop = asyncio.get_event_loop()

    # 将协程转为task任务
    task = loop.create_task(coroutine)
    # loop.create_future(coroutine)

    # 将task任务扔进事件循环对象中并触发
    loop.run_until_complete(task)

async def do_some_work(timeout):
    print('Waiting: ', timeout)
    await asyncio.sleep(timeout)
    return f'Done after {timeout}s'

def tasks1():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)
    tasks = [asyncio.ensure_future(coroutine1),
             asyncio.ensure_future(coroutine2),
             asyncio.ensure_future(coroutine3)]
    loop  = asyncio.get_event_loop()
    
    # asyncio.wait() 返回两个 Task/Future 集合: (done, pending)
    loop.run_until_complete(asyncio.wait(tasks))
    # asyncio.gather() 会把值直接返回，不需要手动去收集
    # loop.run_until_complete(asyncio.gather(*tasks))
    for task in tasks:
        print(f'task result: {task.result()}')

# 外部的协程函数
async def tasks2():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]

    dones, pendings = await asyncio.wait(tasks)

    for task in dones:
        print('Task ret: ', task.result())

def run_tasks2():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks2())

if __name__ == '__main__':
    run_tasks2()