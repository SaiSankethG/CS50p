import sys
import requests
import json

response=requests.get( "https://api.coindesk.com/v1/bpi/currentprice.json")
r=response.json()
for i in r["bpi"]:
    for j in i["USD"]:
        



