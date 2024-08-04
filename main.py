from Class import Class
from Student import Student
from Teacher import Teacher
#commit

if __name__ == "__main__":
    Teacher1 = Teacher("Galyna", "Ivanova", ['Математика', 'Информатика'])
    print(Teacher1._subjects)  # просто посмотреть заполнились ли предметы
    Student1 = Student("Petya", "Savenkov")
    Student2 = Student("Anna", "Smirnova")
    Student3 = Student("Ivan", "Makarov")
    Class1 = Class(Teacher1, [Student1, Student2, Student3])  # создаем класс
    print(len(Class1))  # проверяем что методы работают именно для школьников

    Teacher1.set_class(Class1)  # добавляем этот класс преподавателю
    print(Teacher1.get_class())  # не поняла что понимается под читать класс, вернула просто поле
    Student3.set_class(Class1)  # заполняем школьнику 3 поле класс

    Teacher2 = Teacher("Ivan", "Pushkin", ['Биология', 'Физика'])
    Student4 = Student("Masha", "Larina")
    Student5 = Student("Egor", "Morozov")
    Student6 = Student("Kirill", "Potapov")
    Class2 = Class(Teacher1, [Student4, Student5, Student6])  # создаем класс 2
    print("Class2", Class2)
    Student3.set_class(
        Class2)  # меняем школьнику номер 3 класс, правда сам школьник не удаляется из класса 1, и не добавляется в класс 2 это необходим как-то реализовать особенно или вносить изменения 'вручную'?
    Student3.get_class()
    Class2.append(Student3)  # вручную добавляем школьника в класс 2
    print(len(Class2))
    Class1.remove(Student3)  # вручную удаляем школьника из класса 1
    print(len(Class1))
    if Student2 < Student3:
        print("Студент 1 меньше или равен Студенту 2")
    else:
        print("Студент больше или равен Студенту 2")
    print(repr(Student5))
    print(Class2["L"])
    Teacher2 = Teacher("Ivan", "Borodavkin", ['Химия', 'Физика'])
    Student4 = Student("Anna", "Erofeeva", None, "10A")
    Student5 = Student("Elizaveta", "Berkovich", None, "10A")
    Student6 = Student("Stanislav", "Rudometkin", None, "10A")
    Class3 = Class(Teacher1, [Student4, Student5, Student6])
    print(Class3)
    Class.write_csv('class_data.csv', Class3)
    class_instance = Class.read_csv('class_data.csv')
    print(class_instance)
    print(class_instance._homeroom_teacher.name, class_instance._homeroom_teacher.last_name) #достаем из класса учителя
