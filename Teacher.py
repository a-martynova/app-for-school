from Human import Human
from Subject import Subject
from Class import Class
from typing import List

class Teacher(Human):
   def __init__(self, name : str, last_name : str, _subjects: List[Subject], _homeroom_class: Class | None = None):
      Human.__init__(self, name, last_name)
      self._subjects = _subjects
   def set_class(self, _homeroom_class: Class | None):
        self._homeroom_class = _homeroom_class
   def get_class(self):
        return self._homeroom_class