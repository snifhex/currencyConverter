
import sys
import json
import requests
import argparse

parser = argparse.ArgumentParser(description="Currency ceverter tool")
parser.add_argument('-a', dest='amount', help='Amount we want to convert')
parser.add_argument('-b', dest='base', help='Base currency we are converting from')
parser.add_argument('-t', dest='to_currency', help='Target currency we are converting to')
parser.add_argument('-d', dest='date', help='Date from which we want conversion rates')

args = parser.parse_args()

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
    if args.amount == None:
        amount = int(input("[*]Enter amount > "))
    else:
        amount = int(args.amount)

    if args.base == None:
        base = input("[*]Enter Base Currency > ").upper()
    else:
        base = args.base.upper()

    if args.to_currency == None:
        to_currency = input(
            "[*]Enter the currency you need to convert in > ").upper()
    else:
        to_currency = args.to_currency.upper()

    if args.date == None:
        rates = getRates(base)
    else:
        rates = getRates(base, args.date)
    
    result = convert(amount, to_currency, rates)
    
    print(result)
