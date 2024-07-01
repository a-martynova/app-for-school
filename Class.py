from typing import List

class Class(list):
   def __init__(self, _homeroom_teacher: "Teacher", _students : List["Student"]= []):
          super().__init__(_students)
          self._homeroom_teacher = _homeroom_teacher

   # _grade: int
   # _letter: str
   # ...
   #def __getitem__(self, name):
   #   ...