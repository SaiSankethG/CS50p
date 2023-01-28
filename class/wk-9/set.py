students=[
    {"name":"Harry", "house":"Gryffindor"},
    {"name":"Heromine", "house":"Gryffindor"},
    {"name":"Ron", "house":"Gryffindor"},
    {"name":"Draco", "house":"Slytherin"},
    {"name":"Padma" ,"house":"Ravenclaw"}
]

# houses=[]
# for student in students:
#     if student["house"] not in houses:
#         houses.append(student["house"])
houses=set()
for student in students:
    houses.add(student["house"])

for house in houses:
    print(house)