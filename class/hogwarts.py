students=[{"name":"Heromine" ,"house":"gryffindor" ,"patronus":"otter"},
          {"name":"Harry" , "house":"gryffindor" , "patronus":"stag"},
          {"name":"Ron" , "house":"gryffindor" , "patronus":"jack russell terrir"} ,
          {"name":"Draco" , "house":"slytherin" , "patronus":None}
          ]

for student in students:
    print(student["name"] , student["house"] , student["patronus"] , sep=", ")