from validator_collection import validators

email=validators.email(input("What's your email address?") ,  allow_empty=False)
if email:
    print("Valid")
else:
    print("Invalid")
#print(email)
