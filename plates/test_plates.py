from plates.plates import is_valid

def main():
    test_valid
    test_invalid

def test_valid():
    assert is_valid("CS50")==True

def test_invalid():
    assert is_valid('CS05')==False
    assert is_valid('CS50p')==False
    assert is_valid('H')==None
    assert is_valid('outatime')==None

if __name__=="__main__":
    main()