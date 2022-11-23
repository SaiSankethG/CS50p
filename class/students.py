# with open("names.csv") as file:
#     for line in file:
#         name , college=line.rstrip().split(",")
#         print(f"{name} is in {college}")

students=[]

with open("names.csv") as file:
    for line in file:
        name, college=line.rstrip().split(",")
        student={}
        student={"name":name , "college":college}
        students.append(student)

def getname(student):
    return student["college"]

for student in sorted(students, key=getname):
    print(f"{student['name']} is in {student['college']}")