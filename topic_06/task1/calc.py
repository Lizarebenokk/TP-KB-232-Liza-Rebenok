import logging
from functions import dodav, vidniman, dilena, mnozena

logging.basicConfig(
    filename="calc.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

print('Hello, I am a calculator!')

while True:
    q1 = input('Enter number 1 or "exit" to quit: ')
    if q1.lower() == 'exit':
        logging.info("User exited the program.")
        print("Exiting the program. Goodbye!")
        break
    try:
        q1 = float(q1)
        logging.info(f"Entered number 1: {q1}")
    except ValueError:
        logging.warning("User entered invalid value for number 1.")
        print("Error! Please enter a number.")
        continue

    q2 = input('Enter number 2 or "exit" to quit: ')
    if q2.lower() == 'exit':
        logging.info("User exited the program.")
        print("Exiting the program. Goodbye!")
        break
    try:
        q2 = float(q2)
        logging.info(f"Entered number 2: {q2}")
    except ValueError:
        logging.warning("User entered invalid value for number 2.")
        print("Error! Please enter a number.")
        continue

    v = input('Which operation would you like to perform? \n 1. Addition \n 2. Subtraction \n 3. Division \n 4. Multiplication \n Enter operation number or "exit" to quit: ')
    if v.lower() == 'exit':
        logging.info("User exited the program.")
        print("Exiting the program. Goodbye!")
        break

    try:
        v = int(v)
        logging.info(f"Chosen operation: {v}")
    except ValueError:
        logging.warning("User entered invalid value for operation.")
        print("Error! Please enter the operation number.")
        continue

    if v not in [1, 2, 3, 4]:
        logging.warning(f"User entered invalid operation number: {v}")
        print("Error! Invalid operation number.")
        continue

    match v:
        case 1:
            result = dodav(q1, q2)
            operation = 'addition'
        case 2:
            result = vidniman(q1, q2)
            operation = 'subtraction'
        case 3:
            result = dilena(q1, q2)
            operation = 'division'
        case 4:
            result = mnozena(q1, q2)
            operation = 'multiplication'

    logging.info(f"Operation: {operation}, Numbers: {q1}, {q2}, Result: {result}")
    print(f'Result of {operation} = {result}')
