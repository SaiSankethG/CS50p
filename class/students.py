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

for student in students:
    print(f"{student['name']} is in {student['college']}")