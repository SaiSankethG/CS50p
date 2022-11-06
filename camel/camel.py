# def main():
#     camel_case=input("camelCase:")
#     print("snake_case:")
#     for i in range(len(camel_case)):
#        if (camel_case[i]>="A" and camel_case[i]<="Z"):
#         snake_case=camel_case[i-1].replace("" , "_")
#         snake_case=camel_case[i].lower()
#         print(snake_case ,end="")
#        else:
#          print(snake_case , end="")

# main()

camelCase=input("camelCase:")
print("snake_case:" ,end="")
for i in camelCase:
  if