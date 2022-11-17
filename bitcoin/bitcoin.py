import sys
import requests
import json

if len(sys.argv)==2:
    try:
        value=float(sys.argv[2])
    except:
        print("Command-line argument is not a number")
        sys.exit()
else:
    print("Missing command-line argument")
    sys.exit()

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
r = response.json()
for i in r["bpi"]:
    for j in i["USD"]:
        print(j["rate"])
