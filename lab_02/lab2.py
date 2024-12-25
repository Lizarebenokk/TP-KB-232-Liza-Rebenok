import csv
from sys import argv

students = [
    {"name": "Lili", "surname": "Fiduk", "phone": "0967754765", "email": "Lili@email.com"},
    {"name": "Sasha", "surname": "Suska", "phone": "0636653456", "email": "Sasha@email.com"},
    {"name": "Sofi", "surname": "Derevas", "phone": "069875467", "email": "Sofi@email.com"},
    {"name": "Nada", "surname": "Yops", "phone": "0937598754", "email": "Nada@email.com"},
    {"name": "Kristina", "surname": "Ylot", "phone": "0934421435", "email": "Kristina@email.com"}
]

def load_from_csv(file_name):
    global students
    try:
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            students = list(reader)
            print(f"Data loaded successfully from {file_name}.")
    except FileNotFoundError:
        print(f"File {file_name} not found. Starting with default list.")
    except Exception as e:
        print(f"Error loading file: {e}")

def save_to_csv(file_name):
    try:
        with open(file_name, "w", newline='') as file:
            fieldnames = ["name", "surname", "phone", "email"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
            print(f"Data saved successfully to {file_name}.")
    except Exception as e:
        print(f"Error saving file: {e}")

def printAllList():
    for elem in students:
        strForPrint = f"Student name: {elem['name']} {elem['surname']}, Phone: {elem['phone']}, Email: {elem['email']}"
        print(strForPrint)

def addNewElement():
    global students
    name = input("Please enter student name: ")
    surname = input("Please enter student surname: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")

    newItem = {"name": name, "surname": surname, "phone": phone, "email": email}
    insertPosition = 0

    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)
    print("New element has been added.")

def deleteElement():
    global students
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in students:
        if name == item["name"]:
            deletePosition = students.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        del students[deletePosition]
        print(f"Student {name} has been deleted.")

def updateElement():
    global students
    name = input("Please enter name to be updated: ")
    updatePosition = -1

    for index, item in enumerate(students):
        if item["name"] == name:
            updatePosition = index
            break

    if updatePosition == -1:
        print(f"Student with name {name} not found.")
        return

    print(f"Updating information for student {name} {students[updatePosition]['surname']}:")
    new_name = input(f"Enter new name (current: {students[updatePosition]['name']}): ")
    surname = input(f"Enter new surname (current: {students[updatePosition]['surname']}): ")
    phone = input(f"Enter new phone (current: {students[updatePosition]['phone']}): ")
    email = input(f"Enter new email (current: {students[updatePosition]['email']}): ")

    students[updatePosition]["name"] = new_name if new_name else students[updatePosition]["name"]
    students[updatePosition]["surname"] = surname if surname else students[updatePosition]["surname"]
    students[updatePosition]["phone"] = phone if phone else students[updatePosition]["phone"]
    students[updatePosition]["email"] = email if email else students[updatePosition]["email"]

    print(f"Student {name} has been updated.")

def main():
    if len(argv) > 1:
        load_from_csv(argv[1])

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print, S save, X exit ]: ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated:")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted:")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed:")
                printAllList()
            case "S" | "s":
                save_to_csv("students.csv")
            case "X" | "x":
                print("Exiting program.")
                save_to_csv("students.csv")
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()
