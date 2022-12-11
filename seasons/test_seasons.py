from seasons.seasons import convert

def main():
    test_check_minutes()

def test_check_minutes():
    assert convert("2003-09-01")=="ten million, one hundred thirty-nine thousand forty minutes"
    assert convert("01 september, 2003")=="Invalid Date"

if __name__=="__main__":
    main()

