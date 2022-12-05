def main():
    student=get_student()
    print()

def get_student():
    name=input("Name:")
    house=input("House:")
    return name, house

if __name__=="__main__":
    main()