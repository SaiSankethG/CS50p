email=input("whats your email?").strip()

if "@" in email:
    print("Valid")
else:
    print("Invalid")