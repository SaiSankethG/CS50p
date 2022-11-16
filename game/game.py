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
    number=input("Guess:")
    try:
        if(int(number)<num):
            print("Too small!")
        elif(int(number)>num):
            print("Too large!")
        elif int(number)==num:
            print("Just right!")
            break
    except(ValueError , EOFError):
        pass