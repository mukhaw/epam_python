from datetime import datetime

from hm_1.tasks.task_05_01 import Homework, Student, Teacher


def test_class_homework_atributes_saved():
    attributes = (
        "Learn function",
        datetime(2019, 1, 13, 0, 0, 0),
        datetime(2019, 1, 12, 15, 44, 35),
    )
    test_homework = Homework(*attributes)
    actual_attributes = (
        test_homework.text,
        test_homework.dead_line,
        test_homework.created,
    )
    assert actual_attributes == attributes


def test_class_homework_method_is_active_returns_true():
    attributes = (
        "Learn function",
        datetime(2019, 1, 13, 0, 0, 0),
        datetime(2019, 1, 12, 15, 44, 35),
    )
    assert Homework(*attributes).is_active() is True


def test_class_homework_method_is_active_returns_false():
    attributes = (
        "Learn function",
        datetime(2019, 1, 13, 0, 0, 0),
        datetime(2019, 1, 14, 15, 44, 35),
    )
    assert Homework(*attributes).is_active() is False


def test_class_student_atributes_saved():
    attributes = "Petrov", "Ivan"
    test_student = Student(*attributes)
    actual_attributes = test_student.last_name, test_student.first_name
    assert actual_attributes == attributes


def test_class_student_method_do_homework_returns_homework():
    attributes_for_student = "Petrov", "Ivan"
    attributes_for_homework = (
        "Learn function",
        datetime(2019, 1, 13, 0, 0, 0),
        datetime(2019, 1, 12, 15, 44, 35),
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
        datetime(2019, 1, 13, 0, 0, 0),
        datetime(2019, 1, 13, 15, 44, 35),
    )
    test_student = Student(*attributes_for_student)
    assert test_student.do_homework(Homework(*attributes_for_homework)) == "You're late"


def test_class_teacher_atributes_saved():
    attributes = "Petrova", "Ivanessa"
    test_student = Teacher(*attributes)
    actual_attributes = test_student.last_name, test_student.first_name
    assert actual_attributes == attributes


def test_class_teacher_method_create_homework_returns_homework():
    attributes_for_student = "Petrov", "Ivan"
    attributes_for_homework = (
        "Learn function",
        datetime(2019, 1, 13, 0, 0, 0),
        datetime(2019, 1, 12, 15, 44, 35),
    )
    test_student = Teacher(*attributes_for_student).create_homework(
        *attributes_for_homework
    )
    assert list(test_student.__dict__.values()) == list(
        Homework(*attributes_for_homework).__dict__.values()
    )
