from typing import List

class Class(list):
    def __init__(self, _homeroom_teacher: "Teacher", _students: List["Student"] = []):
        super().__init__(_students)
        self._homeroom_teacher = _homeroom_teacher

    def __getitem__(self, key):
        need_students = [student for student in self if student.last_name.startswith(key) or student.name.startswith(key)]
        return need_students



# _grade: int
   # _letter: str
   # ...
   #def __getitem__(self, name):
   #   ...