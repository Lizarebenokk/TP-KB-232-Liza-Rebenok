import requests

curs = input("Choose curs (EUR, USD, PLN): ").upper()
try:
    value = float(input(f"Enter amount of {curs}: "))
except ValueError:
    print("Error: invalid number entered.")
    exit()

r = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")

if r.status_code != 200:
    print("Error while fetching data from API.")
    exit()

curs_rate = None

for elem in r.json():
    if elem['cc'] == curs:
        curs_rate = elem['rate']
        break

if curs_rate is None:
    print(f"Error: curs {curs} is not supported.")
else:
    result = curs_rate * value
    print(f"One {curs} in UAH: {curs_rate}")
    print(f"Result of {value} {curs} in UAH = {result:.2f}")
