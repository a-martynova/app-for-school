from typing import List
import csv
from Subject import Subject


class Class(list):
    def __init__(self, _grade: int, _letter: str, _homeroom_teacher: "Teacher", _students: List["Student"] = None):
        if _students is None:
            _students = []
        super().__init__(_students)
        self._grade = _grade
        self._letter = _letter
        self._homeroom_teacher = _homeroom_teacher

    def __getitem__(self, key):
        need_students = [student for student in self if
                         student.last_name.startswith(key) or student.name.startswith(key)]
        return need_students

    def __iter__(self):
        return iter(sorted(super().__iter__(), key=lambda student: (student.last_name, student.name)))

    def __str__(self):
        return f"Class {self._grade}{self._letter} Homeroom Teacher: {self._homeroom_teacher.name} {self._homeroom_teacher.last_name}, Students: [{', '.join(str(student.name) + ' ' + str(student.last_name) for student in self)}]"

    def __repr__(self):
        return f"Class(grade={self._grade}, letter='{self._letter}', Homeroom_teacher={repr(self._homeroom_teacher)}, Students={super().__repr__()})"

    @staticmethod
    def write_csv(filename: str, class_instance: "Class"):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(
                ['grade', 'letter', 'Name', 'Last Name', 'id', 'Homeroom Teacher Name', 'Homeroom Teacher Last Name', 'Homeroom Teacher Subjects'])
            for student in class_instance:
                writer.writerow(
                    [class_instance._grade, class_instance._letter, student.name, student.last_name, student.id,
                     class_instance._homeroom_teacher.name,
                     class_instance._homeroom_teacher.last_name, ', '.join([subject.value for subject in class_instance._homeroom_teacher._subjects])])



    @staticmethod
    def read_csv(filename: str):
        from Teacher import Teacher
        from Student import Student

        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            students = []

            for row in reader:
                grade, letter, name, last_name, student_id = row[0], row[1], row[2], row[3], row[4]
                homeroom_teacher = Teacher(name=row[5], last_name=row[6], _subjects=[Subject(subject.strip()) for subject in row[7].split(',')])
                student = Student(name=name, last_name=last_name, id=student_id)
                students.append(student)

            return Class(_grade=grade, _letter=letter, _homeroom_teacher=homeroom_teacher, _students=students)
