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

```
python converter.py 
[*]Enter amount > 45
[*]Enter Base Currency > EUR
[*]Enter the currency you need to convert in > USD
49.4055
```

Or get amount converted directly with optional arguments

```
python converter.py -a 45 -b EUR -t USD
49.4055
```

This way it converts amount (45) from base currency (EUR) to target currency (USD)

You can also get help with

'''
python converter.py -h
'''


## How to use as a module in code

Install the package into your environment by doing:

```
pip install .
```

Example usage in your code:

```
>>> import converter
>>> converter.getRates('USD')
{'GBP': 0.8110483651, 'HKD': 7.8421532016, 'IDR': 14146.4523180618, 'ILS': 3.4842881865, 'DKK': 6.8008015302, 'INR': 70.9003552236, 'CHF': 0.9939885235, 'MXN': 19.5907641862, 'CZK': 23.4456690045, 'SGD': 1.3789051826, 'THB': 30.455414883, 'HRK': 6.7597231078, 'EUR': 0.9108297659, 'MYR': 4.1855360233, 'NOK': 9.1005556062, 'CNY': 7.1497404135, 'BGN': 1.7814008562, 'PHP': 51.7451498315, 'PLN': 3.9388833227, 'ZAR': 15.1603971218, 'CAD': 1.330904454, 'ISK': 123.5995992349, 'BRL': 4.073777211, 'RON': 4.3246197286, 'NZD': 1.5802896439, 'TRY': 5.6931414519, 'JPY': 106.7765734584, 'RUB': 64.7982512068, 'KRW': 1195.3001184079, 'USD': 1.0, 'AUD': 1.4798251207, 'HUF': 303.0877129065, 'SEK': 9.8465251844}
>>> converter.convert(100, 'EUR', converter.getRates('USD'))
91.08
```


## Run in Docker

Build image:

```
docker build -t currency_converter .
```

Run currency_converter:
```
docker run --rm -it currency_converter
```

Run easy_converter:
```
docker run --rm -it currency_converter python3 ./easy_converter.py
```
