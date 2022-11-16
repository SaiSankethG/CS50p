import random

while True:
    level=input("Level: ")
    try:
        if int(level)>0:
            break
    except (ValueError ,IndexError):
        pass
num=random.choice(range(0,3000))
while True:
    number=int(input("Guess:"))
    try:
        if(number<num):
            print("Too small!")
            continue
        elif(number>num):
            print("Too large!")
            continue
        elif number==num:
            print("Just right!")
    except(ValueError):
        pass