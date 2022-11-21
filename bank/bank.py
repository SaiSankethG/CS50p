def main():
   amount=input("Greeting:")
   dollar=amount.lower()
   dollar=value(dollar)
   print(dollar)

def value(greeting):
   if greeting.split()[0].replace("," , "")=="hello":
      return "$0"
   elif greeting[0]=="h" and greeting.split()[0]!="hello":
      return ("$20")
   else:
      return ("$100")

main()