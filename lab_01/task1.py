list = [
    {"name": "Lili", "surname": "Fiduk", "phone": "0967754765", "email": "Lili@email.com"},
    {"name": "Sasha", "surname": "Suska", "phone": "0636653456", "email": "Sasha@email.com"},
    {"name": "Sofi", "surname": "Derevas", "phone": "069875467", "email": "Sofi@email.com"},
    {"name": "Kristina", "surname": "Ylot", "phone": "0934421435", "email": "Kristina@email.com"}
]

def printAllList():
    for elem in list:
        strForPrint = f"Student name: {elem['name']} {elem['surname']}, Phone: {elem['phone']}, Email: {elem['email']}"
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ")
    surname = input("Please enter student surname: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")

    newItem = {"name": name, "surname": surname, "phone": phone, "email": email}

    
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        del list[deletePosition]
        print(f"Student {name} has been deleted.")
    return

def updateElement():
    name = input("Please enter name to be updated: ")
    updatePosition = -1

    for index, item in enumerate(list):
        if item["name"] == name:
            updatePosition = index
            break

    if updatePosition == -1:
        print(f"Student with name {name} not found.")
        return

    print(f"Updating information for student {name} {list[updatePosition]['surname']}:")
    surname = input(f"Enter new surname (current: {list[updatePosition]['surname']}): ")
    phone = input(f"Enter new phone (current: {list[updatePosition]['phone']}): ")
    email = input(f"Enter new email (current: {list[updatePosition]['email']}): ")

    list[updatePosition]["surname"] = surname if surname else list[updatePosition]["surname"]
    list[updatePosition]["phone"] = phone if phone else list[updatePosition]["phone"]
    list[updatePosition]["email"] = email if email else list[updatePosition]["email"]

    print(f"Student {name} has been updated.")
    return

def main():
    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print,  X exit ]: ")
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
            case "X" | "x":
                print("Exiting program.")
                break
            case _:
                print("Wrong choice")

main()
