x  , y, z=input("Expression:").split()
a= float(x)
b=float(z)

# match y:
#     case '+':
#         print(a+b)
#     case '-':
#         print(a-b)
#     case '*':
#         print(a*b)
#     case '/':
#         print(a/b)
if y=='+':
   c=a+b
   print(c)
elif y=='-':
   c=a-b
   print("{c:.1f}")
elif y=='*':
   c=a*b
   print("{c:.1f}")
elif y=='/':
   c=a/b
   print("{c:.1f}")
