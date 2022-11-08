try:
   x=int(input("X:"))

except ValueError:
	print("It is not a integer")
else:
	print(f"x is {x}")