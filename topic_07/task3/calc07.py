from operations07 import VodOperations
from functions07 import DiaFunctions

print('Привіт, я калькулятор!')

while True:
    vodo = VodOperations()
    
    q1 = vodo.get_number('Введіть число 1 або "exit" для виходу: ')
    if q1 == "exit":
        print("Завершення програми. До побачення!")
        break

    q2 = vodo.get_number('Введіть число 2 або "exit" для виходу: ')
    if q2 == "exit":
        print("Завершення програми. До побачення!")
        break

    operation = vodo.get_operation()
    if operation == "exit":
        print("Завершення програми. До побачення!")
        break

    diafun = DiaFunctions(q1, q2)

    match operation:
        case 1:
            result = diafun.dodav()
            operation_name = 'додавання'
        case 2:
            result = diafun.vidniman()
            operation_name = 'віднімання'
        case 3:
            result = diafun.dilena()
            operation_name = 'ділення'
        case 4:
            result = diafun.mnozena()
            operation_name = 'множення'

    print(f'Результат {operation_name} = {result}')
