def main():
    word=input("Input: ")
    word=shorten(word)
    print("Output: " , end="")
    print(word ,end="")
    print()

def shorten(word):
    short=""
    for i in word:
        if i>="A" and i<="Z":
            if i in ["A" , "E" , "I" , "O" , "U" ]:
                continue
            else:
                short=short+i
        # else :
        #     if i in ["a" , "e" , "i" , "o" , "u" ]:
        #         continue
        #     else:
        #         short=short+i
    return short
if __name__=="__main__":
    main()