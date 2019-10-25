#!/usr/bin/env python3
import argparse
import requests

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from typing import Any, Callable, Dict, Optional, Union


def cli() -> None:
    args = _get_args()
    _fill_up_missing_args_in_wizard(args)
    result = convert(args.amount, args.base, args.target, args.date)
    print(f'{args.amount} {args.base} = {result} {args.target}')


def _get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Currency converter tool")
    parser.add_argument('-a', dest='amount', help='Amount you want to convert')
    parser.add_argument('-b', dest='base', help='Base currency you are converting from')
    parser.add_argument('-t', dest='target', help='Target currency you are converting to')
    parser.add_argument('-d', dest='date', help='Date from which you want conversion rates')
    return parser.parse_args()


def _fill_up_missing_args_in_wizard(args: argparse.Namespace) -> None:
    args.amount = _validate_arg(args.amount, "Enter amount", Decimal)
    args.base = _validate_arg(args.base, "Enter base currency symbol").upper()
    args.target = _validate_arg(
        args.target, "Enter target currency symbol (the currency you want to convert to)"
    ).upper()


def _validate_arg(value: Any, msg: str, validator: Optional[Callable[..., Any]] = None) -> Any:
    if not value:
        value = _get_arg_from_input(msg)
    if validator:
        try:
            value = validator(value)
        except (ValueError, TypeError, InvalidOperation):
            print(f'Incorrect value "{value}", try again')
            return _validate_arg(_get_arg_from_input(msg), msg, validator)
    return value


def _get_arg_from_input(msg: str) -> str:
    return input(f'[*] {msg} > ')


def get_rates(base_currency: str, date: Optional[str] = None) -> Dict[str, float]:
    date = date or 'latest'
    url = f'https://api.ratesapi.io/api/{date}?base={base_currency.upper()}'
    api_response = requests.get(url)
    rates_json: Dict[str, Dict[str, float]] = api_response.json()

    try:
        return rates_json['rates']
    except KeyError:
        error_msg = rates_json.get('error') or 'Unknown error'
        raise ValueError(error_msg)


def convert(
        amount: Union[int, str, float, Decimal],
        base_currency: str,
        target_currency: str,
        date: Optional[str] = None,
        decimal_precision: int = 2,
) -> Decimal:
    rates = get_rates(base_currency, date)
    try:
        converted_amount = Decimal(amount) * Decimal(str(rates[target_currency]))
        return converted_amount.quantize(
            Decimal('.1') ** decimal_precision, rounding=ROUND_HALF_UP
        )
    except KeyError:
        raise ValueError(f'No rate available for {target_currency}')
    except InvalidOperation:
        raise ValueError(f'Invalid amount value "{amount}"')


if __name__ == "__main__":
    cli()
