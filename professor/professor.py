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
    m=0
    if level==1:
        while n!=11:
            x=random.choice(range(0,9))
            y=random.choice(range(0,9))
            true_answer=x+y
            for _ in range(3):
                user_answer=int(input(f"{x} + {y} ="))
                if user_answer!=true_answer:
                    print("EEE")
                    m+=1
                else:
                    score+=1
                    break
            if  m==3:
                value=x+y
                print(f"{x} + {y} = {value}")
            n+=1
        print(f"Score: {score}")
    elif level==2:
        while n!=11:
            x=random.choice(range(10,99))
            y=random.choice(range(10,99))
            true_answer=x+y
            for _ in range(3):
                user_answer=int(input(f"{x} + {y} ="))
                if user_answer!=true_answer:
                    print("EEE")
                    m+=1
                else:
                    score+=1
                    break
            if  m==3:
                value=x+y
                print(f"{x} + {y} = {value}")
            n+=1
        print(f"Score: {score}")
    elif level==3:
        while n!=11:
            x=random.choice(range(100,999))
            y=random.choice(range(100,999))
            true_answer=x+y
            for _ in range(3):
                user_answer=int(input(f"{x} + {y} ="))
                if user_answer!=true_answer:
                    print("EEE")
                    m+=1
                else:
                    score+=1
                    break
            if  m==3:
                value=x+y
                print(f"{x} + {y} = {value}")
            n+=1
        print(f"Score: {score}")




if __name__ == "__main__":
    main()