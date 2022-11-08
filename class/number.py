try:
   x=int(input("X:"))

except ValueError:
    print("It is not a integer")

print(f"x is {x}")