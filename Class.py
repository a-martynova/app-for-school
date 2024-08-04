from typing import List
import csv
class Class(list):
    def __init__(self, _homeroom_teacher: "Teacher", _students: List["Student"] = None):
        if _students is None:
            _students = []
        super().__init__(_students)
        self._homeroom_teacher = _homeroom_teacher

    def __getitem__(self, key):
        need_students = [student for student in self if student.last_name.startswith(key) or student.name.startswith(key)]
        return need_students
    def __iter__(self):
        return iter(sorted(super().__iter__(), key=lambda student: (student.last_name, student.name)))

    '''def __iter__(self):
        sorted_students = sorted(self, key=lambda student: (student.name, student.last_name))
        return iter(sorted_students)'''

    @staticmethod
    def write_csv(filename: str, class_instance: "Class"):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Last Name', 'id', 'Homeroom Teacher Name', 'Homeroom Teacher Last Name'])
            for student in class_instance:
                writer.writerow([student.name, student.last_name, student.id, class_instance._homeroom_teacher.name,
                                 class_instance._homeroom_teacher.last_name])

    @staticmethod
    def read_csv(filename: str):
        from Teacher import Teacher
        from Student import Student

        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            students = []

            for row in reader:
                name, last_name, student_id = row[0], row[1], row[2]
                homeroom_teacher = Teacher(name=row[3], last_name=row[4], _subjects=[])
                student = Student(name=name, last_name=last_name, id=student_id)
                students.append(student)

            return Class(_homeroom_teacher=homeroom_teacher, _students=students)
