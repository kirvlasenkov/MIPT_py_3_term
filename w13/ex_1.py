import pickle
import sys
from itertools import cycle
from threading import Thread
from dataclasses import dataclass


@dataclass
class Foo:
    number: int
    word: str


def foo():
    return "foo"


def attempt_to_serialize(types: list):
    serialized_successfully = []
    for t in types:
        try:
            serialized_successfully.append(pickle.dumps(t, protocol=pickle.HIGHEST_PROTOCOL))
        except TypeError:
            print(f"impossible to serialize {type(t)}", file=sys.stderr)
        else:
            print(f"fortunately serialized {type(t)}", file=sys.stderr)

    return serialized_successfully


if __name__ == '__main__':
    types = [
        open("ex_1.txt", "w"),
        cycle([1, 2, 3, 4, 5]),
        Thread,
        Foo,
        Foo(10, "ten"),
        foo,
    ]

    serialized_types = attempt_to_serialize(types=types)

    # example of deserialization
    func_foo = pickle.loads(serialized_types[-1])
    Foo_instance = pickle.loads(serialized_types[-2])
    print("foo result:", func_foo())
    print("Foo result:", Foo_instance.__dict__)

'''
ОТВЕТ ПО ТЕОРИИ:
Из приведенных типов можно сериализовать все,
кроме файлового потока. 

В принципе взаимодействовать со всем можно после
десериализации также как и изначально, единственное
теперь нужно думать о том, чтобы в скрипте был импорт 
модуля, содержащего сериализованный объект, так как
сам pickle сериализует только имя и __dict__ у любого
объекта, и не сможет создать новый объект класса
с заполненными аттрибутами, если нет указания на исходное место
хранения данного класса через импорт модуля
'''
