# with open("names.csv") as file:
#     for line in file:
#         name , college=line.rstrip().split(",")
#         print(f"{name} is in {college}")

students=[]

with open(names.csv) as file:
    for line in file:
        name, college=line.rstrip().split(",")
        students.append(f"{name} is in {college}")

for i in sorted(students):
    print(i)