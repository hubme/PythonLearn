# coding: utf-8

from dataclasses import dataclass
import json


@dataclass
class Person:
    id: str
    name: str
    age: int


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
