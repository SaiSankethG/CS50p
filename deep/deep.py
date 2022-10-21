uni=input("What is the Answer to the Great question of life, the Universe and Everything?")

if uni.strip()=="42":
    print("Yes")
elif uni.lower().strip() == "forty-two":
    print("Yes")
elif uni.lower().strip() == "forty two":
    print("Yes")
else:
    print("No")
