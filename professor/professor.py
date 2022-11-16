import random


def main():
    level=get_level()
    print(level)




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
    print()


if __name__ == "__main__":
    main()