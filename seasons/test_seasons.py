from seasons import convert

def main():
    test_check_minutes()

def test_check_minutes():
    assert convert("2003-09-01")=="Ten million, one hundred eighty-six thousand, five hundred sixty minutes"
    # with pytest.raise(ValueError):
    #     convert()
    assert convert("2021-12-12")=="Five hundred seventy-one thousand, six hundred eighty minutes"
    # assert convert(")

if __name__=="__main__":
    main()

