def main():
  time=input("What time is it? ")
  hours , minutes =time.split(":")
  minute=float(minutes)/60
  hour=float(hours)
  if hour>=7 and hour+minute<=8:
    print("breakfast time")
  elif hour>=12 and hour+minute<=13:
    print("lunch time")
  elif hour>=18 and hour+minute<=19:
    print("dinner time")


main()