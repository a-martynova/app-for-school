class Human:
    _id_set = set()

    def __init__(self, name: str, last_name: str, id=None):
        self.name = name
        self.last_name = last_name
        if id is None:
            self.id = self.generate_id()
        else:
            if id in Human._id_set:
                raise Exception("Переданный id уже существует!")
            self.id = id
            Human._id_set.add(id)

    def generate_id(self):
        new_id = 1
        while new_id in Human._id_set:
            new_id += 1
        Human._id_set.add(new_id)
        return new_id

    def __lt__(self, other):
        return (self.last_name, self.name) < (other.last_name, other.name)

    def __str__(self):
        return f"{self.name} {self.last_name} {self.id}"

    def __repr__(self):
        return f"Human({self.name}, {self.last_name}, {self.id})"

    def __hash__(self):
        return hash((self.id, self.name, self.last_name))
