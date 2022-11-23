# name=input("Whats your name?")

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# with open("names.txt" , "r") as file:
#     for line in sorted(file):
#         print("hello, " , line.rstrip())

name=[]
with open("names.txt") as file:
    for line in file:
        name.append(line.rstrip())

for i in sorted(name , reverse=True):
    print(f"Hello,{i}")