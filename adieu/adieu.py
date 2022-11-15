name=[]

while True:
    try:
        name=input("Name: ")
    except:
        print()
        break
l=len(name)
print("Length:" , l)