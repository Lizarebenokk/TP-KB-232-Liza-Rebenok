test_functions = "  hello, World! this is A TEST functions.  "

results = {
    "strip()": test_functions.strip(),                      # видаляє пробіли
    "capitalize()": test_functions.lstrip().capitalize(),   # пропускає пробіли
    "title()": test_functions.title(),                      # кожне слово починається з великої літери
    "upper()": test_functions.upper(),                      # перетворює всі символи на великі літери
    "lower()": test_functions.lower(),                      # перетворює всі символи на малі літери
}

print(
    "strip(): " + results["strip()"] + "\n" +
    "capitalize(): " + results["capitalize()"] + "\n" +
    "title(): " + results["title()"] + "\n" +
    "upper(): " + results["upper()"] + "\n" +
    "lower(): " + results["lower()"]
)

