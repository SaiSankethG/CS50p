class Wizard:
    

class Student(Wizard):
    def __init__(self , name, house):
        super().__init__(name)
        self.house=house


class Professor(Wizard):
    def __init__(self , name , subject):
        super().__init__(name)
        self.subject=subject


