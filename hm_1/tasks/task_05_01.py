"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime
1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean
2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None
3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
from datetime import datetime


class Homework:
    def __init__(self, text, dead_line, created):
        self.text = text
        self.dead_line = dead_line
        self.created = created

    def is_active(self) -> bool:
        return datetime.now() < self.dead_line + self.created


class Student:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, hw: Homework):
        if not hw.is_active():
            print("You're late")
            return None
        return hw


class Teacher:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def create_homework(text, dead_line, created) -> Homework:
        return Homework(text, dead_line, created)
