email=input("whats your email?").strip()

if "@" and "." in email:
    print("Valid")
else:
    print("Invalid")