import unittest
from student import Student
from studentList import StudentList

class TestStudentList(unittest.TestCase):
    def setUp(self):
        self.studentList = StudentList()
        self.student = Student("John", "Doe", "123-456-7890", "john@example.com")

    def test_add_student(self):
        self.studentList.addStudent(self.student)
        self.assertEqual(len(self.studentList.students), 1)
        self.assertEqual(self.studentList.students[0].first_name, "John")
        self.assertEqual(self.studentList.students[0].last_name, "Doe")

    def test_delete_student(self):
        self.studentList.addStudent(self.student)
        self.studentList.deleteStudent("John Doe")
        self.assertEqual(len(self.studentList.students), 0)

    def test_update_student(self):
        self.studentList.addStudent(self.student)
        self.studentList.updateStudent("John Doe", new_first_name="Jane", new_last_name="Doe")
        self.assertEqual(self.studentList.students[0].first_name, "Jane")
        self.assertEqual(self.studentList.students[0].last_name, "Doe")

    def test_print_all(self):
        self.studentList.addStudent(self.student)
        from io import StringIO
        import sys
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        self.studentList.printAll()
        sys.stdout = sys.__stdout__
        self.assertIn("John Doe", capturedOutput.getvalue())

if __name__ == '__main__':
    unittest.main()
