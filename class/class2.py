class Student:
    def __init__(self , name, house):  #it is dunder init method.it is should contain a default name.
        if not name:
            raise ValueError("Missing Name")
        if house not in["Gryffindor" , "Slytherin" , "Ravenclaw" , "Hufflepuff"]:
            raise ValueError("Invalid House")
        self.name=name
        self.house=house
    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student=get_student()
    print(student)

def get_student():
    name=input("Name: ")
    house=input("House:")
    student=Student(name ,house)  #constructor when the Student is called it will be created.
    return student

if __name__=="__main__":
    main()