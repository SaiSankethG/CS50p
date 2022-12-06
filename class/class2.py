class Student:
    def __init__(self , name, house ):  #it is dunder init method.it is should contain a default name.
        if not name:
            raise ValueError("Missing Name")
        self.name=name
        self.house=house
    def __str__(self):
        return f"{self.name} from {self.house}"
    @property
    def name(self):
        return self._name
    @name.setter
    def house(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name=name

    @property
    #getter
    def house(self):
        return self._house

    @house.setter
    #setter
    def house(self , house):
        if house not in ["Gryffindor" , "Revanclaw", "Slytherin" , "Hufflepuf"]:
            raise ValueError("Invalid house")
        self._house=house


def main():
    student=get_student()
    #student.house="Blue"
    print(student)

def get_student():
    name=input("Name: ")
    house=input("House:")
    student=Student(name ,house )  #constructor when the Student is called it will be created.
    return student

if __name__=="__main__":
    main()