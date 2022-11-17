import sys
import requests
import json

if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    r = response.json()
    true_value=float(r["bpi"]["USD"]["rate_float"])
    user_value=true_value*value
    print(f"${user_value:,.4f}")
except requests.RequestException:
    print("RequestException")
    sys.exit(1)
