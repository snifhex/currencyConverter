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