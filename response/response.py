import re
from validator_collection import validators, checkers, errors

email=input("whats your email?").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(edu)$" , email , re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")