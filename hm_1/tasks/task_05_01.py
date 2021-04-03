class Homework:
    def __init__(self, text, dead_line, created):
        self.text = text
        self.dead_line = dead_line
        self.created = created

    def is_active(self) -> bool:
        return self.created < self.dead_line


class Student:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(
        self,
    ):
        ...


class Teacher:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def create_homework(self, text, dead_line, created):
        return Homework(text, dead_line, created)


if __name__ == "__main__":
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    teacher.last_name = "Daniil"
    student.first_name = "Petrov"

    expired_homework = teacher.create_homework("Learn functions", 0)
    expired_homework.created = (
        "2019-05-26 16:44:30.688762"  # Example: 2019-05-26 16:44:30.688762
    )
    expired_homework.deadline = "0:00:00"
    expired_homework.text = "Learn functions"

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    oop_homework.deadline = "5 days, 0:00:00"
