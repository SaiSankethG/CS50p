class Student:
    def __int__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name:")
    house = input("Input:")
    return Student(name, house)


if __name__ == "__main":
    main()
