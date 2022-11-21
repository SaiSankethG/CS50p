def main():
    word=input("Input: ")
    word=shorten(word)
    print("Output: " , end="")
    print(word ,end="")
    print()

def shorten(word):
    short=NULL
    for i in word:
        if i>="A" and i<="Z":
            if i in ["A" , "E" , "I" , "O" , "U" ]:
                continue
            else:
                short=i+short
        else :
            if i in ["a" , "e" , "i" , "o" , "u" ]:
                continue
            else:
                short=i+short
    return short
if __name__=="__main__":
    main()