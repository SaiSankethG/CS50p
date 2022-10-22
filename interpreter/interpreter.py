x  , y, z=input("Expression:").split()
a= float(x)
b=float(z)

if y=='+':
   print(f"{a+b:.1f}")
elif y=='-':
   print(f"{a-b:.1f}")
elif y=='*':
   print(f"{a*b:.1f}")
elif y=='/':
   print(f"{a/b:.1f}")
