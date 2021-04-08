from datetime import datetime, timedelta

from hm_1.tasks.task_05_01 import Homework, Student, Teacher


def test_class_homework_atributes_saved():
    attributes = (
        "Learn function",
        timedelta(days=5),
        datetime(2019, 1, 12, 15, 44, 35),
    )
    assert list(Homework(*attributes).__dict__.values()) == list(attributes)


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
    attributes = "Petrov", "Ivan"
    assert list(Student(*attributes).__dict__.values()) == list(attributes)


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
    test_student = Student(*attributes_for_student)
    assert test_student.do_homework(Homework(*attributes_for_homework)) == (
        "You're late",
        None,
    )


def test_class_teacher_atributes_saved():
    attributes = "Petrova", "Ivanessa"
    assert list(Teacher(*attributes).__dict__.values()) == list(attributes)


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
