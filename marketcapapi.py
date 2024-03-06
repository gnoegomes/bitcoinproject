# -*- coding: utf-8 -*-
"""
Made by:Gabriel Noé
"""

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'1',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'faf61372-4992-4359-876e-89231aa8f497',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  "print(data)"
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

def data_gather(name, tipo="data" ):
    dict1 = data[tipo]
    for dicts in dict1:
        if dicts.get("name") == name:
            print(dicts)
            break
        else:
            print(dicts.get("name"))
            print("Valor não encontrado")
    


data_gather("Bitcoin")
