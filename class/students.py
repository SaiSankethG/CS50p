# with open("names.csv") as file:
#     for line in file:
#         name , college=line.rstrip().split(",")
#         print(f"{name} is in {college}")

students=[]

with open("names.csv") as file:
    for line in file:
        name, college=line.rstrip().split(",")
        student={}
        student["name"]=name
        student["house"]=house
        students.append(student)

