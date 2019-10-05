
import sys
import json
import requests


def getRates(base_curreny):
    url = f'https://api.ratesapi.io/api/latest?base={base_curreny}'
    api_response = requests.get(url)
    rates_json = api_response.json()
    conversion_rates = rates_json['rates']
    return conversion_rates


def availabe_currencies(rates):
    currencies = list(rates)
    return currencies


def convert(amount, desired_currency, conversion_rates):
    converted_amount = conversion_rates[desired_currency] * amount
    return converted_amount


if __name__ == "__main__":
    if len(sys.argv) == 4:
        amount = sys.argv[1]
        base = sys.argv[2]
        to_currency = sys.argv[3]

        rates = getRates(base)
        result = convert(amount, to_currency, rates)
        print(result)

    elif len(sys.argv) == 2:
        if sys.argv[1].upper() == "HELP":
            print(availabe_currencies)

    else:
        amount = int(input("[*]Enter amount > "))
        base = input("[*]Enter Base Currency > ").upper()
        to_currency = input(
            "[*]Enter the currency you need to convert in > ").upper()
        rates = getRates(base)
        result = convert(amount, to_currency, rates)
        print(result)
