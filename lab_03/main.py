import sys
from student import Student
from studentList import StudentList
from file import FileHandler

def main():
    studentList = StudentList()
    fileHandler = FileHandler()

    if len(sys.argv) > 1:
        fileHandler.loadFromCsv(sys.argv[1], studentList)
    else:
        print("No file specified, starting with an empty student list.")
    
    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print, X exit ]: ")
        if choice.lower() == "c":
            first_name = input("Please enter student first name: ")
            last_name = input("Please enter student last name: ")
            phone = input("Please enter student phone: ")
            email = input("Please enter student email: ")
            student = Student(first_name, last_name, phone, email)
            studentList.addStudent(student)
        elif choice.lower() == "u":
            name = input("Please enter the full name of the student to be updated (first name last name): ")
            new_first_name = input("Enter new first name (leave blank to keep current): ") or None
            new_last_name = input("Enter new last name (leave blank to keep current): ") or None
            phone = input("Enter new phone (leave blank to keep current): ") or None
            email = input("Enter new email (leave blank to keep current): ") or None
            studentList.updateStudent(name, new_first_name, new_last_name, phone, email)
        elif choice.lower() == "d":
            name = input("Please enter the full name (first name last name) of the student to be deleted: ")
            studentList.deleteStudent(name)
        elif choice.lower() == "p":
            studentList.printAll()
        elif choice.lower() == "x":
            if len(sys.argv) > 1: 
                fileHandler.saveToCsv(sys.argv[1], studentList)
            print("Exit()")
            break
        else:
            print("Wrong choice")

if __name__ == "__main__":
    main()
