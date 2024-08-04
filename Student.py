from Human import Human
from Class import Class

class Student(Human):
    def __init__(self, name: str, last_name: str, id=None, _class: "Class"=None):
        super().__init__(name, last_name, id)
        self._class = _class

    def set_class(self, _class):
        self._class = _class

    def get_class(self):
        return self._class

    def __str__(self):
        return f"Student: {self.name} {self.last_name}, id: {self.id}, Class: {self._class}"

    def __repr__(self):
        return f"Student({self.name}, {self.last_name}, id={self.id}, class={self._class})"


