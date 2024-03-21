import sys
import requests
import json


if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    quantity = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number ")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
except requests.RequestException:
    sys.exit("Request Exception Occured...")

# print(json.dumps(response, indent=3))

try:
    price = response["bpi"]["USD"]["rate_float"]
except KeyError:
    sys.exit("Key Error Occured...")

total = price * quantity
print(f"${total:,.4f}")
sys.exit(0)
