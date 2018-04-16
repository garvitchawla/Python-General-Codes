import json
import urllib.request
from pprint import pprint

# Grabbing data from a public API. Yahoo Finance where it converts currency rates.
# parse that data.
# This API converts USD to other currencies.

# urlopen function used to open a Webpage. Take it as a response and then .read() that response.

with urllib.request.urlopen('http://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json') as response:
    source = response.re

pprint(source)

data = json.loads(source)

print(json.dumps(data, indent=2))

usd_rates = dict()

for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price

print(50 * float(usd_rates['USD/INR']))
