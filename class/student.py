class Student:
    def __int__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name=input("Name: ")
        house=input("Input:")
        return cls(name , house)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main":
    main()
