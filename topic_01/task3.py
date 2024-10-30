#Завдання №3: написати функцію пошуку дискримінанту
def descr (a, b, c):
    result = b**2 - 4*a*c
    return result

a = float(input("What's a: "))
b = float(input("What's b: "))
c = float(input("What's c: "))  


print("Result of the discriminant: ", descr(a, b, c))
