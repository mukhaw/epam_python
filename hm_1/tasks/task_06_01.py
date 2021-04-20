"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""
from itertools import count


def get_created_instances(cls):
    return next(cls._ids) if cls else 0


def reset_instances_counter(cls):
    cls._ids = count(0)
    return get_created_instances(cls) - 1


def instances_counter(cls):
    """Some code"""
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter
    return cls


@instances_counter
class User(object):
    _ids = count(0)

    def __init__(self):
        self.id = next(self._ids)
