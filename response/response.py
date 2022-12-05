from validator_collection import validators , errors

try:
    email=validators.email(input("What's your email address?") ,  allow_empty=False)
    print("Valid")
except (errors.InvalidEmailError):
    print("Invalid")

# if email:
#     print("Valid")
# else:
#     print("Invalid")
#print(email)
