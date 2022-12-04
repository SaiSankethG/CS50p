import re
from validator_collection import validators, checkers, errors

email=input("whats your email?").strip()

# username , domain=email.split("@")

# if username and "." in domain:
#     print("Valid")
# else:
#     print("Invalid")
if re.search(r"^\w+@(\w+\.)?\w+\.(edu)$" , email , re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")