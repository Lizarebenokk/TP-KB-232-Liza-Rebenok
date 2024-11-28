from functions import dodav, vidniman, dilena, mnozena
from operations import get_number, get_operation

print('Привіт, я калькулятор!')

while True:
    q1 = get_number('Введіть число 1 або "exit" для виходу: ')
    if q1 == "exit":
        print("Завершення програми. До побачення!")
        break

    q2 = get_number('Введіть число 2 або "exit" для виходу: ')
    if q2 == "exit":
        print("Завершення програми. До побачення!")
        break

    operation = get_operation()
    if operation == "exit":
        print("Завершення програми. До побачення!")
        break

    match operation:
        case 1:
            result = dodav(q1, q2)
            operation_name = 'додавання'
        case 2:
            result = vidniman(q1, q2)
            operation_name = 'віднімання'
        case 3:
            result = dilena(q1, q2)
            operation_name = 'ділення'
        case 4:
            result = mnozena(q1, q2)
            operation_name = 'множення'

    print(f'Результат {operation_name} = {result}')
