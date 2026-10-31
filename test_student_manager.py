import unittest
from student import Student
from student_manager import StudentManager


class TestStudentManager(unittest.TestCase):

    def setUp(self):
        self.manager = StudentManager()
        self.student = Student(1, "Hardik", 21, "Python")

    def test_add_student(self):
        self.manager.add_student(self.student)
        self.assertIn(1, self.manager.students_info)

    def test_search_existing_student(self):
        self.manager.add_student(self.student)
        result = self.manager.search_student(1)
        self.assertEqual(result.name, "Hardik")

    def test_search_nonexistent_student(self):
        result = self.manager.search_student(99)
        self.assertIsNone(result)

    def test_delete_student(self):
        self.manager.add_student(self.student)
        result = self.manager.delete_student(1)
        self.assertTrue(result)
        self.assertNotIn(1, self.manager.students_info)

    def test_delete_nonexistent_student(self):
        result = self.manager.delete_student(99)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()