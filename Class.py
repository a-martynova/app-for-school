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


    @staticmethod
    def write_csv(filename: str, class_instance: "Class"):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Last Name'])
            for student in class_instance:
                writer.writerow([student.name, student.last_name])


# _grade: int
   # _letter: str
   # ...
   #def __getitem__(self, name):
   #   ...