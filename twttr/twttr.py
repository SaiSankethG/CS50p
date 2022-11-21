def main():
    word=input("Input: ")
    shorten(word)
    print("Output: " , end="")
    print()

def shorten(word):
    for i in word:
        if i>="A" and i<="Z":
            if i in ["A" , "E" , "I" , "O" , "U" ]:
                continue
            else:
                
        else :
            if i in ["a" , "e" , "i" , "o" , "u" ]:
                continue
            else:
                print(i , end="")