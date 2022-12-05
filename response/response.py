from validator_collection import validators

try:
    email=validators.email(input("What's your email address?") ,  allow_empty=False)
    print("Valid")
except (InvalidEmailError , ValueError):
    print("Invalid")

# if email:
#     print("Valid")
# else:
#     print("Invalid")
#print(email)
