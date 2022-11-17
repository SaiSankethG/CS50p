import sys
import requests
import json

response=requests.get( https://api.coindesk.com/v1/bpi/currentprice.json)
r=response.json()
print(r)

