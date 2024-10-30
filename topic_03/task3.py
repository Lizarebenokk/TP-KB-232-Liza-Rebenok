def t_slov_functions():
    my_slov = {}
    print("Початковий словник:", my_slov)

    while True:
        print("\nВиберіть функцію словника для тестування:")
        print("1. update()")
        print("2. del (видалити ключ)")
        print("3. clear()")
        print("4. keys()")
        print("5. values()")
        print("6. items()")
        print("7. Показати словник")
        print("8. Вийти")

        choice = input("Введіть номер операції: ")

        match choice:
            case '1':
                keys_values = input("Введіть ключі та значення для оновлення у форматі 'ключ=значення', розділені комою: ")
                update_dict = dict(item.split('=') for item in keys_values.split(','))
                my_slov.update(update_dict)
                print("Словник після update():", my_slov)

            case '2':
                key = input("Введіть ключ для видалення: ")
                try:
                    del my_slov[key]
                    print("Словник після видалення ключа:", my_slov)
                except KeyError:
                    print("Помилка: Ключ не знайдено у словнику.")

            case '3':
                my_slov.clear()
                print("Словник очищено:", my_slov)

            case '4':
                keys = my_slov.keys()
                print("Ключі словника:", list(keys))

            case '5':
                values = my_slov.values()
                print("Значення словника:", list(values))

            case '6':
                items = my_slov.items()
                print("Елементи словника (ключ, значення):", list(items))

            case '7':
                print("Поточний словник:", my_slov)

            case '8':
                print("Завершення програми.")
                break

            case _:
                print("Невірний вибір. Спробуйте ще раз.")

t_slov_functions()
