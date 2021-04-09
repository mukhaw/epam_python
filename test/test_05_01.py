import io
import sys
from datetime import datetime, timedelta

from hm_1.tasks.task_05_01 import Homework, Student, Teacher


def test_class_homework_atributes_saved():
    test_homework = Homework(
        "Learn function",
        timedelta(days=5),
        datetime(2019, 1, 12, 15, 44, 35),
    )
    assert test_homework.text == "Learn function"
    assert test_homework.dead_line == timedelta(days=5)
    assert test_homework.created == datetime(2019, 1, 12, 15, 44, 35)


def test_class_homework_method_is_active_returns_true():
    attributes = (
        "Learn function",
        timedelta(days=5),
        datetime(2021, 4, 12, 15, 44, 35),
    )
    assert Homework(*attributes).is_active() is True


def test_class_homework_method_is_active_returns_false():
    attributes = (
        "Learn function",
        timedelta(days=0),
        datetime(2019, 1, 14, 15, 44, 35),
    )
    assert Homework(*attributes).is_active() is False


def test_class_student_atributes_saved():
    test_student = Student("Petrov", "Ivan")
    assert test_student.last_name == "Petrov"
    assert test_student.first_name == "Ivan"


def test_class_student_method_do_homework_returns_homework():
    attributes_for_student = "Petrov", "Ivan"
    attributes_for_homework = (
        "Learn function",
        timedelta(days=3),
        datetime(2021, 4, 8, 15, 44, 35),
    )
    test_student = Student(*attributes_for_student).do_homework(
        Homework(*attributes_for_homework)
    )
    assert list(test_student.__dict__.values()) == list(
        Homework(*attributes_for_homework).__dict__.values()
    )


def test_class_student_method_do_homework_returns_message():
    attributes_for_student = "Petrov", "Ivan"
    attributes_for_homework = (
        "Learn function",
        timedelta(days=5),
        datetime(2019, 1, 13, 15, 44, 35),
    )
    captured_output = io.StringIO()  # Create StringIO object
    sys.stdout = captured_output
    test_student = Student(*attributes_for_student).do_homework(
        Homework(*attributes_for_homework)
    )
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().rstrip("\n") == "You're late"
    assert test_student is None


def test_class_teacher_atributes_saved():
    attributes = "Petrova", "Ivanessa"
    test_teacher = Teacher(*attributes)
    assert test_teacher.last_name == "Petrova"
    assert test_teacher.first_name == "Ivanessa"


def test_class_teacher_method_create_homework_returns_homework():
    attributes_for_student = "Petrov", "Ivan"
    attributes_for_homework = (
        "Learn function",
        timedelta(days=9),
        datetime(2021, 4, 12, 15, 44, 35),
    )
    test_student = Teacher(*attributes_for_student).create_homework(
        *attributes_for_homework
    )
    assert list(test_student.__dict__.values()) == list(
        Homework(*attributes_for_homework).__dict__.values()
    )
