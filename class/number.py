while True:
	try:
   x=int(input("X:"))

except ValueError:
	print("It is not a integer")
else:
	break
print(f"x is {x}")