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
    homework = Homework(
        "Learn function",
        timedelta(days=5),
        datetime(2021, 4, 12, 15, 44, 35),
    )
    assert homework.is_active() is True


def test_class_homework_method_is_active_returns_false():
    homework = Homework(
        "Learn function",
        timedelta(days=0),
        datetime(2019, 1, 14, 15, 44, 35),
    )
    assert homework.is_active() is False


def test_class_student_atributes_saved():
    test_student = Student("Petrov", "Ivan")
    assert test_student.last_name == "Petrov"
    assert test_student.first_name == "Ivan"


def test_class_student_method_do_homework_returns_homework():
    student = Student("Petrov", "Ivan")
    homework = Homework(
        "Learn function",
        timedelta(days=3),
        datetime(2022, 4, 8, 15, 44, 35),
    )
    assert student.do_homework(homework) == homework


def test_class_student_method_do_homework_returns_message(capsys):
    student = Student("Petrov", "Ivan")
    homework = Homework(
        "Learn function",
        timedelta(days=5),
        datetime(2019, 1, 13, 15, 44, 35),
    )
    doing_homework = student.do_homework(homework)
    assert capsys.readouterr().out == "You're late\n"
    assert doing_homework is None


def test_class_teacher_atributes_saved():
    teacher = Teacher("Petrova", "Ivanessa")
    assert teacher.last_name == "Petrova"
    assert teacher.first_name == "Ivanessa"


def test_class_teacher_method_create_homework_returns_homework():
    teacher = Teacher("Petrov", "Ivan")
    attributes = (
        "Learn function",
        timedelta(days=9),
        datetime(2021, 4, 12, 15, 44, 35),
    )
    assert list(teacher.create_homework(*attributes).__dict__.values()) == list(
        attributes
    )
