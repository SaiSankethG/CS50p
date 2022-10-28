def main():
  time=input("Whats the time?")
  hours , minutes =time.split(":")
  minute=minutes/60
  if hours>=7 and hours+minute<=8:
    print("breakfast time")
  elif hours>=12 and hours+minute<=13:
    print("lunch time")
  elif hours>=18 and hours+minute<=19:
    print("dinner time")


main()