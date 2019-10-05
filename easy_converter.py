import sys
import json
import requests


def convert(amount, base, to):
    url = f'https://api.ratesapi.io/api/latest?base={base}&symbols={to}'
    response = requests.get(url).json()
    return float(response['rates'][to])*float(amount)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        amount = sys.argv[1]
        base = sys.argv[2].upper()
        to_currency = sys.argv[3].upper()

    else:
        amount = int(input("[*]Enter amount > "))
        base = input("[*]Enter Base Currency > ").upper()
        to_currency = input(
            "[*]Enter the currency you need to convert in > ").upper()

    result = convert(amount, base, to_currency)
    print(result)
