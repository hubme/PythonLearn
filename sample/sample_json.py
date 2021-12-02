# coding: utf-8

"""" https://docs.python.org/zh-cn/3/library/dataclasses.html """

from dataclasses import dataclass, field
import json


# frozen = True 表示对象是不可变对象，初始化完成之后，不可对成员重新赋值
# order = True，会生成__lt__(), __le__(), __gt__(), __ge__()方法
# 如果 eq 和 frozen 都是 True，则会生成 __hash__ 方法
# 当自定义了 __init__()时，init 参数会被忽略
@dataclass(frozen=True)
class Person:
    id: str
    name: str
    age: int
    sex: bool = field(compare=False)  # 标记此字段不参比较


def json2obj():
    json_str = '{"age": 18, "id": "111", "name": "Vance"}'
    obj = json.loads(json_str, object_hook=lambda dict: Person(dict['id'], dict['name'], dict['age']))
    print(obj, f'id: {obj.id}, name: {obj.name}, age: {obj.age}')


def obj2json():
    json_text = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
    obj = json.dumps(json_text)  # 对象转字符串
    print(obj)

    p = Person('111', 'Vance', 18)
    # TypeError: Object of type Person is not JSON serializable
    # print(json.dumps(p))

    # 字段不排序
    print(json.dumps(p, default=vars))

    # 字段排序，按照键的 ASCII码来排序
    print(json.dumps(p, default=vars, sort_keys=True))

    # lambda obj: obj.__dict__： 会将任意的对象，转换成字典的方式
    print(json.dumps(p, default=lambda obj: obj.__dict__, indent=4))


if __name__ == '__main__':
    obj2json()
