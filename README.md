# currencyConverter

Command line currency converter. 

Under the hood, conversion rates are obtained from this API: https://api.ratesapi.io

## How to install

(optionally), create a virtualenv: 

```
virtualenv ~/.venvs/currencyconverter
source ~/.venvs/currencyconverter/bin/activate
```

Install dependencies: 

```
pip install requests
```


## How to use


Simply launch the main python script and follow on screen instructions: 
```
python converter.py 
```

E.g.:

```bash
python converter.py 
[*] Enter amount you want to convert > 42.42
[*] Enter base currency code you are converting from > eur
[*] Enter target currency code you are converting to > usd
42.42 EUR = 47.20 USD  (date: latest)
```

Or get amount converted directly with optional arguments

```bash
python converter.py -a 42.42 -b EUR -t USD
42.42 EUR = 47.20 USD  (date: latest)
```

This way it converts amount (45) from base currency (EUR) to target currency (USD).

If you only need amount in return (e.g. command used in pipe), use `-s` flag:
```bash
python converter.py -a 45 -b EUR -t USD -d 2018-01-01 -s
53.97
```

If any argument is missing or is invalid the wizard is launched.

```bash
./converter.py -a 42.42 -b EUR -t USD -d 2019-01-32
Incorrect value "2019-01-32": unconverted data remains: 2, try again...
[*] Enter date from which you want conversion rates, in format yyyy-mm-dd or string "latest" > 2019-01-23
42.42 EUR = 48.22 USD  (date: 2019-01-23)
```

You can also get help with

```bash
python converter.py -h
usage: converter.py [-h] [-a AMOUNT] [-b BASE] [-t TARGET] [-d DATE] [-s]

Currency converter tool

optional arguments:
  -h, --help           show this help message and exit
  -a AMOUNT            Amount you want to convert
  -b BASE              Base currency code you are converting from
  -t TARGET            Target currency code you are converting to
  -d DATE              Date from which you want conversion rates, in format
                       YYYY-MM-DD or string "latest" (default: latest)
  -s, --simple-output  If present, only converted amount is returned
```


## How to use as a module in code

Install the package into your environment by doing:

```
pip install .
```

Example usage in your code:

```python
>>> import converter
>>> converter.convert(42.42, 'usd', 'hrk', '2012-12-24')
Decimal('242.11')
>>> converter.convert(42.42, 'usd', 'hrk', '2012-12-24', decimal_precision=6)
Decimal('242.106582')
>>> converter.get_rates('USD')
{'GBP': 0.8110483651, 'HKD': 7.8421532016, 'IDR': 14146.4523180618, 'ILS': 3.4842881865, 
'DKK': 6.8008015302, 'INR': 70.9003552236, 'CHF': 0.9939885235, 'MXN': 19.5907641862, 
'CZK': 23.4456690045, 'SGD': 1.3789051826, 'THB': 30.455414883, 'HRK': 6.7597231078, 
# [...]
'USD': 1.0, 'AUD': 1.4798251207, 'HUF': 303.0877129065, 'SEK': 9.8465251844}
```


## Run in Docker

Build image:

```bash
docker build -t currency_converter .
```

Run currency_converter:
```bash
docker run --rm -it currency_converter
[wizard questionare...]
```
or
```bash
docker run --rm -it currency_converter bash -c "./converter.py -a 45 -b USD -t GBP"
45 USD = 35.09 GBP  (date: latest)
```
