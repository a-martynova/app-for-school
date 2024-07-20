class Human:
    _id_set = set()  # Множество для хранения всех существующих id

    def __init__(self, name: str, last_name: str, id=None):
        self.name = name
        self.last_name = last_name
        if id is None:
            self.__id = self.generate__id()
        else:
            if id in Human._id_set:
                raise Exception("Переданный id уже существует!")
            self.__id = id
            Human._id_set.add(id)

    def generate__id(self):
        new_id = 1
        while new_id in Human._id_set:
            new_id += 1
        Human._id_set.add(new_id)
        return new_id

    def __lt__(self, other):
        return (self.last_name, self.name) < (other.last_name, other.name)

    def __str__(self):
        return f"{self.name} {self.last_name} {self.__id}"

    def __repr__(self):
        return f"Human({self.name}, {self.last_name}, {self.__id})"

    def __hash__(self):
        return hash((self.__id, self.name, self.last_name))





