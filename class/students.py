# with open("names.csv") as file:
#     for line in file:
#         name , college=line.rstrip().split(",")
#         print(f"{name} is in {college}")
import csv
students=[]

with open("names.csv") as file:
    # for line in file:
    #     name, college=line.rstrip().split(",")
    #     student={}
    #     student={"name":name , "college":college}
    #     students.append(student)
    
for student in sorted(students, key=lambda student:student["name"]):
    print(f"{student['name']} is in {student['college']}")