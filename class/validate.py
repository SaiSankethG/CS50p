import re

email=input("whats your email?").strip()

# username , domain=email.split("@")

# if username and "." in domain:
#     print("Valid")
# else:
#     print("Invalid")
if re.search("..*@..*" , email):
    print("Valid")
else:
    print("Invalid")