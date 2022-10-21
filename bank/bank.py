amount=input("Greeting:")
dollar=amount.lower()

if dollar.split()[0]=="hello":
   print("$0")
elif dollar[0]=="h" and dollar.split()[0]!="hello":
   print("$20")
else:
   print("$100")