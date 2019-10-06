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
python converter.py 45 EUR USD
49.4055
```

This way it converts amount (45) from base currency (EUR) to target currency (USD)


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
