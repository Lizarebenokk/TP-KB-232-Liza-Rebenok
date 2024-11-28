class Chel:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

Chelovek = Chel("Liza", 18)
print(str(Chelovek))
