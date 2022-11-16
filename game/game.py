import 

while True:
    level=input("Level: ")
    try:
        if int(level)>0:
            break
    except ValueError:
        pass
