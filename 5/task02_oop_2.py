"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


class DeadlineError(Exception):
    """Raised in case of the late hw submission"""
    pass


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.now()

    def is_active(self):
        return datetime.datetime.now() < (self.created + self.deadline)


class HomeworkResult:
    def __init__(self, author, homework: Homework, solution: str):
        if isinstance(homework, Homework):
            self.homework = homework
        else:
            raise TypeError('Given object is NOT a "Homework" object')
        self.solution = solution
        self.author = author
        self.created = datetime.datetime.now()


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):
    def do_homework(self, homework: Homework, solution: str):
        if homework.is_active():
            hw_done = HomeworkResult(self, homework, solution)
            return hw_done
        else:
            raise DeadlineError("You are late.")


class Teacher(Person):
    homework_done = defaultdict(list)

    @staticmethod
    def create_homework(text, deadline):
        return Homework(text, deadline)

    @classmethod
    def check_homework(cls, hw_result: HomeworkResult):
        hw = hw_result.homework
        if len(hw_result.solution) > 5 and hw_result not in cls.homework_done:
            cls.homework_done[hw].append(hw_result)
            return True
        else:
            return False

    @classmethod
    def reset_results(cls, hw=None):
        if isinstance(hw, Homework):
            cls.homework_done.pop(hw)

        elif hw is None:
            cls.homework_done.clear()
        else:
            raise TypeError('this method takes only a "Homework" object as an argument')