from sys import argv

if len(argv)<2:
    exit("Too few arguments")
elif len(argv)>2:
    exit("Too many arguments")

print("Hello , my name is" , argv[1])