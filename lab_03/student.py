class Student:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Student Name: {self.first_name} {self.last_name}, Phone: {self.phone}, Email: {self.email}"
