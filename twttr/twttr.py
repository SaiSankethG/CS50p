word=input("Input: ")
print("Output: " , end="")
for i in word:
    if i>="A" and i<="Z":
        if i in ["A" , "E" , "I" , "O" , "U" ]:
            continue
        else:
            print(i , end="")
    else :
        if i in ["a" , "e" , "i" , "o" , "u" ]:
            continue
        else:
            print(i , end="")

print()