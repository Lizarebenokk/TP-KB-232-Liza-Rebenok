def get_number(prompt):
    while True:
        num = input(prompt)
        if num.lower() == "exit":
            return "exit"
        try:
            return float(num)
        except ValueError:
            print("Помилка! Будь ласка, введіть число.")

def get_operation():
    while True:
        operation = input('Яку саме операцію вам треба провести? \n 1. Додавання \n 2. Віднімання \n 3. Ділення \n 4. Множення \n Введіть номер операції або "exit" для виходу: ')
        if operation.lower() == "exit":
            return "exit"
        try:
            operation = int(operation)
            if operation in [1, 2, 3, 4]:
                return operation
            else:
                print("Помилка! Невірний номер операції.")
        except ValueError:
            print("Помилка! Будь ласка, введіть номер операції.")
