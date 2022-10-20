name=input("Whats your name?")

match name:
    case "Harry" | "Heromine" | "Ron":
      print("Griffonder")
    case "Draco":
      print("Slytherin")
    case _:
      print("who?")
      
