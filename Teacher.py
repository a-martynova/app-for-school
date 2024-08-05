from Human import Human
from Subject import Subject
from Class import Class
from typing import List
from Class import Class

class Teacher(Human):
    def __init__(self, name: str, last_name: str, _subjects: List[Subject], __homeroom_class: Class | None = None):
        Human.__init__(self, name, last_name)
        self.__homeroom_class = None
        self._subjects = _subjects

    def set_class(self, __homeroom_class: Class | None):
        self.__homeroom_class = __homeroom_class

    def get_class(self):
        return self.__homeroom_class

    def __repr__(self):
        return f"Teacher({self.name}, {self.last_name}, {self._subjects}, homeroom_class={self.__homeroom_class})"

    def __str__(self):
        if self.__homeroom_class is not None:
            return f"Teacher: {self.name} {self.last_name}, Subjects: {[subject.name for subject in self._subjects]}, Class: {self.__homeroom_class._grade}{self.__homeroom_class._letter}"
        else:
            return f"Teacher: {self.name} {self.last_name}, Subjects: {[subject.name for subject in self._subjects]}, Homeroom Class: {self.__homeroom_class}"


