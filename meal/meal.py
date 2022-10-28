def main():
  time=input("Whats the time?")
  hours , minutes =time.split(":")
  minute=float(minutes/60)
  hour=float(hours)
  if hour>=7 and hours+minute<=8:
    print("breakfast time")
  elif hour>=12 and hours+minute<=13:
    print("lunch time")
  elif hour>=18 and hours+minute<=19:
    print("dinner time")


main()