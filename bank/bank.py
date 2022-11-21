def main():
   amount=input("Greeting:")
   dollar=amount.lower()
   dollar=value(dollar)
   print(dollar)

def value(greeting):
   greeting=greeting.lower()
   if greeting.split()[0].replace("," , "")=="hello":
      return "$0"
   elif greeting[0]=="h" and greeting.split()[0]!="hello":
      return ("$20")
   else:
      return ("$100")

if __name__=="__main_":
   main()