"""
Python 中类的构造方法 __new__ 的使用
https://mp.weixin.qq.com/s/2XT2izhpKJ0TpYd5NUG7ig
"""


class A:
    def __new__(cls, *args, **kwargs):
        print("new", cls, args, kwargs)
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print("init", self, args, kwargs)


def how_object_construction_works():
    x = A(1, 2, 3, x=4)
    print(x)
    print("===================")

    x = A.__new__(A, 1, 2, 3, x=4)
    if isinstance(x, A):
        type(x).__init__(x, 1, 2, 3, x=4)
    print(x)


class UppercaseTuple(tuple):
    """ 应用1：改变内置的不可变类型 """
    def __new__(cls, iterable):
        upper_iterable = (s.upper() for s in iterable)
        return super().__new__(cls, upper_iterable)

    # 以下代码会报错，初始化时是无法修改的
    # def __init__(self, iterable):
    #     print(f'init {iterable}')
    #     for i, arg in enumerate(iterable):
    #         self[i] = arg.upper()


class Singleton:
    """ 应用2：实现一个单例 """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class Client:
    """ 应用3：客户端缓存 """
    _loaded = {}
    _db_file = "file.db"

    def __new__(cls, client_id):
        if (client := cls._loaded.get(client_id)) is not None:
            print(f"returning existing client {client_id} from cache")
            return client
        client = super().__new__(cls)
        cls._loaded[client_id] = client
        client._init_from_file(client_id, cls._db_file)
        return client

    def _init_from_file(self, client_id, file):
        # lookup client in file and read properties
        print(f"reading client {client_id} data from file, db, etc.")
        name = ...
        email = ...
        self.name = name
        self.email = email
        self.id = client_id


if __name__ == "__main__":
    # how_object_construction_works()
    # print(UppercaseTuple(["hello", "world"]))

    print("SINGLETON EXAMPLE")
    x = Singleton()
    y = Singleton()
    print(f"{x is y=}")