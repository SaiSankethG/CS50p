def main():
  answer=input("What time is it?")
  time=convert(answer)


def convert(time):
  hours , minutes=time.split(":")
  new_minute=minutes/60
  return hours+new_minute



if __name__ == "__main__":
    main()
