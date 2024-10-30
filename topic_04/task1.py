def dodav(a, b):
    return a + b

def vidniman(a, b):
    return a - b

def dilena(a, b):
    if b != 0:
        return a / b
    else:
        return "Помилка! На 0 ділити не можна."

def mnozena(a, b):
    return a * b

print('Привіт, я калькулятор!')

while True:
    q1 = input('Введіть число 1 або "exit" для виходу: ')
    if q1.lower() == 'exit':
        print("Завершення програми. До побачення!")
        break
    try:
        q1 = float(q1)
    except ValueError:
        print("Помилка! Будь ласка, введіть число.")
        continue

    q2 = input('Введіть число 2 або "exit" для виходу: ')
    if q2.lower() == 'exit':
        print("Завершення програми. До побачення!")
        break
    try:
        q2 = float(q2)
    except ValueError:
        print("Помилка! Будь ласка, введіть число.")
        continue

    v = input('Яку саме операцію вам треба провести? \n 1. Додавання \n 2. Віднімання \n 3. Ділення \n 4. Множення \n Введіть номер операції або "exit" для виходу: ')
    if v.lower() == 'exit':
        print("Завершення програми. До побачення!")
        break

    try:
        v = int(v)
    except ValueError:
        print("Помилка! Будь ласка, введіть номер операції.")
        continue

    if v not in [1, 2, 3, 4]:
        print("Помилка! Невірний номер операції.")
        continue

    match v:
        case 1:
            result = dodav(q1, q2)
            operation = 'додавання'
        case 2:
            result = vidniman(q1, q2)
            operation = 'віднімання'
        case 3:
            result = dilena(q1, q2)
            operation = 'ділення'
        case 4:
            result = mnozena(q1, q2)
            operation = 'множення'

    print(f'Результат {operation} = {result}')
