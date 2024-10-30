def t_list_fun():
    t_list = []

    while True:
        print("\nПоточний список:", t_list)
        print("Оберіть операцію для списку:")
        print("1 - extend()")
        print("2 - append()")
        print("3 - insert()")
        print("4 - remove()")
        print("5 - clear()")
        print("6 - sort()")
        print("7 - reverse()")
        print("8 - copy()")
        print("9 - вихід")

        choice = input("Введіть номер операції: ")

        match choice:
            case "1":
                elements = input("Введіть елементи для додавання через пробіл: ").split()
                t_list.extend(elements)
                print("Результат після extend():", t_list)

            case "2":
                element = input("Введіть елемент для додавання: ")
                t_list.append(element)
                print("Результат після append():", t_list)

            case "3":
                index = int(input("Введіть індекс для вставки елемента: "))
                element = input("Введіть елемент для вставки: ")
                t_list.insert(index, element)
                print("Результат після insert():", t_list)

            case "4":
                element = input("Введіть елемент для видалення: ")
                if element in t_list:
                    t_list.remove(element)
                    print("Результат після remove():", t_list)
                else:
                    print("Елемент не знайдено!")

            case "5":
                t_list.clear()
                print("Список очищено:", t_list)

            case "6":
                t_list.sort()
                print("Результат після sort():", t_list)

            case "7":
                t_list.reverse()
                print("Результат після reverse():", t_list)

            case "8":
                copied_list = t_list.copy()
                print("Копія списку:", copied_list)

            case "9":
                print("Завершення програми.")
                break

            case _:
                print("Невірна команда! Спробуйте ще раз.")

t_list_fun()
