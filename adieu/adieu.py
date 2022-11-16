name=[]

while True:
    try:
        name=input("Name: ")
    except:
        print()
        break
if "liesl" in name:
    print("Adieu, adieu, to Liesl")
elif "Friedrich , Liesl" in name:
    print("Adieu, adieu, to Liesl and Friedrich")
elif "Liesl, Friedrich, Louisa" in name:
    print("")