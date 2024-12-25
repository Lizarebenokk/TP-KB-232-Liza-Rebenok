class StudentList:
    def __init__(self):
        self.students = []

    def addStudent(self, student):
        insert_position = 0
        for i in range(len(self.students)):
            if (student.first_name + " " + student.last_name).lower() > (self.students[i].first_name + " " + self.students[i].last_name).lower():
                insert_position += 1
            else:
                break
        self.students.insert(insert_position, student)
        print(f"New student has been added: {student.first_name} {student.last_name}")

    def deleteStudent(self, full_name):
        delete_position = -1
        for i, student in enumerate(self.students):
            if (student.first_name + " " + student.last_name).lower() == full_name.lower():
                delete_position = i
                break
        if delete_position != -1:
            del self.students[delete_position]
            print(f"Student with name {full_name} has been deleted.")
        else:
            print(f"No student with name {full_name} found.")

    def updateStudent(self, full_name, new_first_name=None, new_last_name=None, phone=None, email=None):
        student = next((s for s in self.students if (s.first_name + " " + s.last_name).lower() == full_name.lower()), None)
        if not student:
            print("Student was not found.")
            return

        if new_first_name:
            student.first_name = new_first_name
        if new_last_name:
            student.last_name = new_last_name
        if phone:
            student.phone = phone
        if email:
            student.email = email
        print(f"Information about {full_name} has been updated.")

    def printAll(self):
        if not self.students:
            print("Student list is empty.")
        for student in self.students:
            print(student)