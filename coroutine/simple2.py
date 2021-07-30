import asyncio
import threading
import time


"""
https://docs.python.org/zh-cn/3/library/asyncio-stream.html
"""

# @asyncio.coroutine
async def hello():
    print('%s: hello, world!' % threading.current_thread())
    # 休眠不会阻塞主线程因为使用了异步I/O操作
    # 注意有yield from才会等待休眠操作执行完成
    await asyncio.sleep(2)
    # asyncio.sleep(1)
    # time.sleep(1)
    print('%s: goodbye, world!' % threading.current_thread())


def test1():
    loop = asyncio.get_event_loop()
    tasks = [hello(), hello()]
    print('begin!')
    # 等待两个异步I/O操作执行结束
    loop.run_until_complete(asyncio.wait(tasks))
    print('game over!')
    loop.close()


async def wget(host):
    # print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    # 异步方式等待连接结果
    reader, writer = await connect
    header = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'
    writer.write(header.encode('utf-8'))
    # 异步I/O方式执行写操作
    await writer.drain()
    while True:
        # 异步I/O方式执行读操作
        line = await reader.readline()
        if line == b'\r\n':
            break
        print(line.decode('utf-8').rstrip())
    writer.close()


def test_wget():
    loop = asyncio.get_event_loop()
    # 通过生成式语法创建一个装了三个协程的列表
    # hosts_list = ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']
    hosts_list = ['www.sina.com.cn']
    tasks = [wget(host) for host in hosts_list]
    # 下面的方法将异步I/O操作放入EventLoop直到执行完毕
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    test_wget()