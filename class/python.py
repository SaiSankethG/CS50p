class Wizard:
    def __init__(self ,name):
        self.name=name
    def __str__(self):
        return self.name

class Student(Wizard):
    def __init__(self , name, house):
        super().__init__(name)
        self.house=house
    def __str__(self):
        return f"{self.name} is in {self.house}"


class Professor(Wizard):
    def __init__(self , name , subject):
        super().__init__(name)
        self.subject=subject
    def __str__(self):
        return f"{self.name} subject is {self.subject}"

wizard=Wizard("Albus")
print(wizard)
student=Student("Harry" , "Gryffindor")
print(student)
professor=Professor("Snape" ,"Defense aganist the dark arts")
print(professor)
