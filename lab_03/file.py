import csv
from student import Student

class FileHandler:
    def loadFromCsv(self, file_name, student_list):
        try:
            with open(file_name, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    first_name = row['first_name']
                    last_name = row['last_name']
                    phone = row['phone']
                    email = row['email']
                    student = Student(first_name, last_name, phone, email)
                    student_list.addStudent(student)
            print(f"Data successfully loaded from {file_name}")
        except FileNotFoundError:
            print(f"File {file_name} not found. Starting with an empty student list.")

    def saveToCsv(self, file_name, student_list):
        print(f"Saving to {file_name}...")
        with open(file_name, mode='w', newline='') as file:
            fieldnames = ["first_name", "last_name", "phone", "email"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in student_list.students:
                print(f"Saving student: {student.first_name} {student.last_name}")
                writer.writerow({
                    "first_name": student.first_name,
                    "last_name": student.last_name,
                    "phone": student.phone,
                    "email": student.email
                })
        print(f"Data successfully saved to {file_name}")
