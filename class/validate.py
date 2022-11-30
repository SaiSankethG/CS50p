import re

email=input("whats your email?").strip()

# username , domain=email.split("@")

# if username and "." in domain:
#     print("Valid")
# else:
#     print("Invalid")
if re.search(r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9._]+\.edu$" , email):
    print("Valid")
else:
    print("Invalid")