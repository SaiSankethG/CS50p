import inflect
names=[]

while True:
    try:
        name=input("Name: ")
        names.append(name)
    except:
        print()
        break
if "liesl" in name:
    print("Adieu, adieu, to Liesl")
elif "Friedrich , Liesl" in name:
    print("Adieu, adieu, to Liesl and Friedrich")
elif "Liesl, Friedrich, Louisa" in name:
    print("")