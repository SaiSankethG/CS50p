def meow(n: int)->str:
    return "meow\n"*n

num: int=int(input("Number: "))
meows: str=meow(num)
print(meows, end="")