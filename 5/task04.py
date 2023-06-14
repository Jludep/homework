"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


import functools


def instances_counter(cls):

    @functools.wraps(cls, updated=())
    class DecoratedClass(cls):
        counter = 0

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            DecoratedClass.counter += 1

        @classmethod
        def get_created_instances(cls):
            return cls.counter

        @classmethod
        def reset_instances_counter(cls):
            memorized_counter = cls.counter
            cls.counter = 0
            return memorized_counter
    return DecoratedClass


@instances_counter
class User:
    pass