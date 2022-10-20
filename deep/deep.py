uni=input("What is the answer to the great question of life, the Universe , and Everything?")

# if uni=:
#     print("Yes")
# else :
#     print("No")

match uni:
    case 42 | "forty-two" |"forty two":
        print("Yes")
    case _:
        print("No")