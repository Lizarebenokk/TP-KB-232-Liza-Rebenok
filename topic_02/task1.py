def poshyk_koreniv(a, b, c):
    if a == 0:
        print("Помилка: не є квадратним рівнянням!")
    else:
        D = b**2 - 4*a*c
        print("Дискримінант D:", D)

        if D < 0:
            print("Рівняння не має дійсних коренів")
        elif D == 0:
            x1 = -b / (2*a)
            x2 = -(-b / (2*a))
            print("Рівняння має подвійний корінь:", x1, x2)
        else:
            x1 = (-b + D**0.5) / (2 * a)
            x2 = (-b - D**0.5) / (2 * a)
            print("Рівняння має два корені: ", x1, x2)

a = int(input("Введіть a: ")) 
b = int(input("Введіть b: "))
c = int(input("Введіть c: "))
    
poshyk_koreniv(a, b, c)
