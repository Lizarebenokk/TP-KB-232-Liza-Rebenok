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
q1 = int(input('Введіть число 1: '))
q2 = int(input('Введіть число 2: '))

v = int(input('Яку саме операцію вам треба провести? \n 1. Додавання \n 2. Віднімання \n 3. Ділення \n 4. Множення \n'))

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
    case _:
        result = 'Помилка! Операція невірна.'
        operation = 'невідома операція'

print(f'Результат {operation} = {result}')
