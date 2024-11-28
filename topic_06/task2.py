students = [
    {"name": "Irisha", "grade": 100},
    {"name": "Liza", "grade": 45},
    {"name": "Andrey", "grade": 60},
    {"name": "Kate", "grade": 84}
]

sorted_name = sorted(students, key=lambda student: student["name"])
print("Sorted name:", sorted_name)

sorted_grade = sorted(students, key=lambda student: student["grade"])
print("Sorted grade:", sorted_grade)
