from Human import Human
from Class import Class

class Student(Human):
  def __init__(self, name : str, last_name : str, _class: Class = None):
      Human.__init__(self, name, last_name)
      self._class = _class
  def set_class(self, _class : Class ):
        self._class = _class
  def get_class(self):
        return self._class