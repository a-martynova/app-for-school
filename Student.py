from Human import Human
from Class import Class

class Student(Human):
    def __init__(self, name: str, last_name: str, id=None, __class: "Class"=None):
        super().__init__(name, last_name, id)
        self.__class = __class

    def set_class(self, __class):
        self.__class = __class

    def get_class(self):
        return self.__class

    def __str__(self):
        return f"Student: {self.name} {self.last_name}, id: {self.id}, Class: {self.__class}"

    def __repr__(self):
        return f"Student({self.name}, {self.last_name}, id={self.id}, class={self.__class})"


