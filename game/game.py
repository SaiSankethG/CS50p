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
        elif(number>num):
            print("Too large!")
        elif number==num:
            print("Just right!")
            break
    except(ValueError):
        pass