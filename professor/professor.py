import random


def main():
    level=get_level()
    print(level)
    generate_integer(level)

def get_level():
    while True:
        try:
            level=int(input("Level:"))
            if level in [1, 2 , 3]:
                return level
            else:
                pass
        except:
            pass

def generate_integer(level):
    score=0
    n=1
    while n!=10:
        x=random.choice(range(0,9))
        y=random.choice(range(0,9))
        true_answer=x+y
        user_answer=input(f"{x}+{y}:")
        for _ in range(3):
            



if __name__ == "__main__":
    main()