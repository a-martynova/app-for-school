import unittest
from Class import Class
from Student import Student
from Teacher import Teacher
from Subject import Subject


class TestSchoolSystem(unittest.TestCase):

    def setUp(self):
        # Создаем тестовые данные
        self.teacher1 = Teacher("Galyna", "Ivanova", [Subject.HISTORY])
        self.student1 = Student("Petya", "Savenkov")
        self.student2 = Student("Anna", "Smirnova")
        self.student3 = Student("Ivan", "Makarov")
        self.class1 = Class("11", "A", self.teacher1, [self.student1, self.student2, self.student3])
        self.teacher2 = Teacher("Ivan", "Pushkin", [Subject.INFORMATICS, Subject.MATH])
        self.student4 = Student("Masha", "Larina")
        self.student5 = Student("Egor", "Morozov")
        self.student6 = Student("Kirill", "Potapov")
        self.class2 = Class("8", "B", self.teacher2, [self.student4, self.student5, self.student6])

    def test_set_class_for_student(self):
        self.student1.set_class(self.class1)
        self.assertEqual(self.student1.get_class(), self.class1)
        self.student2.set_class(self.class1)
        self.assertEqual(self.student2.get_class(), self.class1)
        self.student3.set_class(self.class1)
        self.assertEqual(self.student3.get_class(), self.class1)

    def test_set_class_for_teacher(self):
        self.teacher1.set_class(self.class1)
        self.assertEqual(self.teacher1.get_class(), self.class1)

    def test_teacher(self):
        self.assertEqual(self.teacher1.name, "Galyna")
        self.assertEqual(self.teacher1.last_name, "Ivanova")
        self.assertEqual(self.teacher1._subjects, [Subject.HISTORY])

    def test_class(self):
        self.assertEqual(self.class1._grade, "11")
        self.assertEqual(self.class1._letter, "A")
        self.assertEqual(self.class1._homeroom_teacher, self.teacher1)
        self.assertEqual(len(self.class1), 3)

    def test_move_student_to_class(self):
        self.class2.remove(self.student4)  # удалим student4 из class2
        self.assertNotIn(self.student4, self.class2)
        self.class1.append(self.student4)  # перенесем student4 в class1 (сейчас она в class2)
        self.assertIn(self.student4, self.class1)
        self.student4.set_class(self.class1)  # поменяем student4 класс на class1
        self.assertEqual(self.student4.get_class(), self.class1)
        self.assertEqual(len(self.class1), 4)
        # заметка: в файл class1 запишется так как заявлен в setUp, так как setUp вызывается перед каждым тестом.

    def test_student_lt(self):
        self.assertTrue(self.student1 < self.student2)

    def test_find_students(self):  # проверяем поиск студентов по 1 букве имени/ фамилии
        self.assertEqual(self.class2["L"], [self.student4])

    def test_csv(self):
        Class.write_csv('class_data.csv', self.class1)
        class_instance = Class.read_csv('class_data.csv')
        self.assertEqual(class_instance._grade, "11")
        self.assertEqual(class_instance._letter, "A")
        self.assertEqual(len(class_instance), len(self.class1))
        self.assertEqual(class_instance._homeroom_teacher.name, self.teacher1.name)
        self.assertEqual(class_instance._homeroom_teacher._subjects, self.teacher1._subjects)
        
# if __name__ == '__main__':
#     unittest.main()
