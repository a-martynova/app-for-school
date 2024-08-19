from Human import Human


class Student(Human):
    def __init__(self, name: str, last_name: str, id=None, __class: "Class" = None):
        super().__init__(name, last_name, id)
        self.__class = __class

    def set_class(self, __class):
        self.__class = __class

    def get_class(self):
        return self.__class

    def __repr__(self):
        return f"Student(name='{self.name}', last_name='{self.last_name}', id='{self.id}', __class ='{self.__class})"

    def __str__(self):
        if self.__class is not None:
            return f"Student_name: {self.name} {self.last_name}, id: {self.id}, Class: {self.__class._grade} {self.__class._letter}"
        else:
            return f"Student: {self.name} {self.last_name}, id: {self.id}"
