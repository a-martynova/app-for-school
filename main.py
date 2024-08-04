from Class import Class
from Student import Student
from Teacher import Teacher
from Subject import Subject

Teacher1 = Teacher("Galyna", "Ivanova", [Subject.HISTORY])
print(Teacher1._subjects)  # просто посмотреть заполнились ли предметы
Student1 = Student("Petya", "Savenkov")
Student2 = Student("Anna", "Smirnova")
Student3 = Student("Ivan", "Makarov")
Class1 = Class(Teacher1, [Student1, Student2, Student3])  # создаем класс
print(len(Class1))  # проверяем что методы работают именно для школьников
Teacher1.set_class(Class1)  # добавляем этот класс преподавателю
print(Teacher1.get_class())  # не поняла что понимается под читать класс, вернула просто поле
Student3.set_class(Class1)  # заполняем школьнику 3 поле класс
print(Student3.get_class()) #возвращаем класс школьника 3
Student1.set_class(Class1)
Student2.set_class(Class1)
print(Class1)


Teacher2 = Teacher("Ivan", "Pushkin", [Subject.INFORMATICS, Subject.MATH])
Student4 = Student("Masha", "Larina")
Student5 = Student("Egor", "Morozov")
Student6 = Student("Kirill", "Potapov")
Class2 = Class(Teacher1, [Student4, Student5, Student6])  # создаем класс 2
Student4.set_class(Class2)
Student5.set_class(Class2)
Student6.set_class(Class2)
Teacher2.set_class(Class2)  # добавляем этот класс преподавателю
Student3.set_class(Class2)  # меняем школьнику 3 класс
print("Class2", Class2)
Class2.append(Student3)  # добавляем школьника номер 3 в класс 2
print("Class2", Class2)
print(len(Class2))
Class1.remove(Student3)  # удаляем школьника 3 из класса 1
print(len(Class1))

if Student2 < Student3:
    print("Студент 1 меньше или равен Студенту 2")
else:
    print("Студент больше или равен Студенту 2")

print(repr(Student5))
print("name start L", Class2["L"]) # ищем в классе 2 ученика/ учеников с именем или фамилией на L

Teacher3 = Teacher("Ivan", "Borodavkin", [Subject.BIOLOGY, Subject.CHEMISTRY])
Student7 = Student("Anna", "Erofeeva")
Student8 = Student("Elizaveta", "Berkovich")
Student9 = Student("Stanislav", "Rudometkin")
Class3 = Class(Teacher3, [Student7, Student8, Student9])
Teacher3.set_class(Class3)
Student7.set_class(Class3)
Student8.set_class(Class3)
Student9.set_class(Class3)

print(Class3)
Class.write_csv('class_data.csv', Class3) #записываем класс
class_instance = Class.read_csv('class_data.csv') #читаем класс
print(class_instance)
print(class_instance._homeroom_teacher.name, class_instance._homeroom_teacher.last_name) #достаем из класса учителя
