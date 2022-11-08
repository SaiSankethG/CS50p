def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 6>=len(s)>=2 and s[0:2].isalpha() ands.isalnum():
        return True
    else:
        return False
    

main()