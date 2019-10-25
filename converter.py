#!/usr/bin/env python3
import argparse
from datetime import datetime

import requests

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from typing import Any, Callable, Dict, Optional, Union


LATEST = "latest"
AMOUNT_HELP = "Amount you want to convert"
BASE_HELP = "Base currency code you are converting from"
TARGET_HELP = "Target currency code you are converting to"
DATE_HELP = f'Date from which you want conversion rates, in format YYYY-MM-DD or string "{LATEST}"'


def convert(
    amount: Union[int, str, float, Decimal],
    base_currency: str,
    target_currency: str,
    date: Optional[str] = None,
    decimal_precision: int = 2,
) -> Decimal:
    rates = get_rates(base_currency, date)
    target_currency = target_currency.upper()
    try:
        converted_amount = Decimal(amount) * Decimal(str(rates[target_currency]))
        return converted_amount.quantize(Decimal(".1") ** decimal_precision, rounding=ROUND_HALF_UP)
    except KeyError:
        raise ValueError(f"No rate available for {target_currency}")
    except InvalidOperation:
        raise ValueError(f'Invalid amount value "{amount}"')


def get_rates(base_currency: str, date: Optional[str] = None) -> Dict[str, float]:
    date = date or LATEST
    url = f"https://api.ratesapi.io/api/{date}?base={base_currency.upper()}"
    api_response = requests.get(url)
    rates_json: Dict[str, Dict[str, float]] = api_response.json()

    try:
        return rates_json["rates"]
    except KeyError:
        error_msg = rates_json.get("error") or "Unknown error"
        raise ValueError(error_msg)


def cli() -> None:
    args = _get_args()
    _fill_up_missing_args_in_wizard(args)
    result = convert(args.amount, args.base, args.target, args.date)
    if args.simple_output:
        print(result)
    else:
        print(f"{args.amount} {args.base} = {result} {args.target}  (date: {args.date})")


def _get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Currency converter tool")
    parser.add_argument("-a", dest="amount", help=AMOUNT_HELP)
    parser.add_argument("-b", dest="base", help=BASE_HELP)
    parser.add_argument("-t", dest="target", help=TARGET_HELP)
    parser.add_argument("-d", dest="date", help=f"{DATE_HELP} (default: {LATEST})", default=LATEST)
    parser.add_argument(
        "-s",
        "--simple-output",
        help="If present, only converted amount is returned",
        action="store_true",
    )
    return parser.parse_args()


def _fill_up_missing_args_in_wizard(args: argparse.Namespace) -> None:
    args.amount = _validate_arg(args.amount, AMOUNT_HELP, Decimal)
    args.base = _validate_arg(args.base, BASE_HELP, _validate_currency).upper()
    args.target = _validate_arg(args.target, TARGET_HELP, _validate_currency).upper()
    args.date = _validate_arg(args.date, DATE_HELP, _validate_date)


def _validate_arg(value: Any, help_msg: str, validator: Optional[Callable[..., Any]] = None) -> Any:
    if not value:
        value = _get_arg_from_input(help_msg)
    if validator:
        try:
            value = validator(value)
        except (ValueError, TypeError, InvalidOperation) as err:
            print(f'Incorrect value "{value}": {err}, try again...')
            return _validate_arg(_get_arg_from_input(help_msg), help_msg, validator)
    return value


def _get_arg_from_input(msg: str) -> str:
    return input(f"[*] Enter {msg.lower()} > ")


def _validate_currency(currency_code: str) -> str:
    if len(currency_code) != 3 or not currency_code.isalpha():
        raise ValueError("Currency code should be 3 letters long")
    return currency_code


def _validate_date(date: str) -> str:
    if date == LATEST:  # special case
        return date
    else:
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            raise


if __name__ == "__main__":
    cli()
