
import sys
import json
import requests


def getRates(base_currency, date='latest'):
    url = f'https://api.ratesapi.io/api/{date}?base={base_currency}'
    api_response = requests.get(url)
    rates_json = api_response.json()

    if 'rates' in rates_json:
        conversion_rates = rates_json['rates']
        return conversion_rates
    else:
        error = rates_json['error'] if 'error' in rates_json else 'Unknown error'
        raise ValueError(error)


def available_currencies(rates):
    currencies = list(rates)
    return currencies


def convert(amount, desired_currency, conversion_rates):
    if desired_currency in conversion_rates:
        converted_amount = float(
            conversion_rates[desired_currency]) * float(amount)
        return round(converted_amount, 2)
    else:
        raise ValueError(f'No rate available for {desired_currency}')


if __name__ == "__main__":
    if len(sys.argv) == 5:
        amount = sys.argv[1]
        base = sys.argv[2].upper()
        to_currency = sys.argv[3].upper()
        date = sys.argv[4]

        rates = getRates(base, date)
        result = convert(amount, to_currency, rates)
        print(result)

    elif len(sys.argv) == 4:
        amount = sys.argv[1]
        base = sys.argv[2].upper()
        to_currency = sys.argv[3].upper()

        rates = getRates(base)
        result = convert(amount, to_currency, rates)
        print(result)

    elif len(sys.argv) == 2:
        if sys.argv[1].upper() == "HELP":
            print(available_currencies)

    else:
        amount = int(input("[*]Enter amount > "))
        base = input("[*]Enter Base Currency > ").upper()
        to_currency = input(
            "[*]Enter the currency you need to convert in > ").upper()
        rates = getRates(base)
        result = convert(amount, to_currency, rates)
        print(result)
