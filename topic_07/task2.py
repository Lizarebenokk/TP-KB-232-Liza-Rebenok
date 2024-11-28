class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

students = [
    Student("Dima", 21),
    Student("Andrey", 19),
    Student("Sophia", 18),
    Student("Tanya", 17),
    Student("Roma", 23)
]

sorted_students_age = sorted(students, key=lambda student: student.age)

print("Students sorted age:")
for student in sorted_students_age:
    print(student)

sorted_students_name = sorted(students, key=lambda student: student.name)

print("\nStudents sorted name:")
for student in sorted_students_name:
    print(student)
