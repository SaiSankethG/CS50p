from seasons.seasons import convert

def main():
    check_minutes()

def check_minutes():
    assert convert("2003-09-01")=="ten million, one hundred thirty-nine thousand forty minutes"
    assert convert("01 september, 2003")==None

if __name__=="__main__":
    main()

