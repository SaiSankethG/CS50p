students=[
    {"name":"Harry", "house":"Gryffindor"},
    {"name":"Heromine", "house":"Gryffindor"},
    {"name":"Ron", "house":"Gryffindor"},
    {"name":"Draco", "house":"Slytherin"},
    {"name":"Padma" ,"house":"Ravenclaw"}
]

houses=[]
for student in students:
    if students["house"] not in houses:
        houses.append(students["house"])

for house in houses:
    print(house)