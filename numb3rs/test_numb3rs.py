from numb3rs.numb3rs import validate
import sys

def main():
    test_char()
    test_out_of_range()
    test_range()
    sys.exit(0)

def test_char():
    assert validate("cat")==False
    assert validate("dog")==False
def test_out_of_range():
    assert validate("277.0.0.1")==False
    assert validate("255.255.255.288")==False
    assert validate("127.0.0.1111")==False
def test_range():
    assert validate("127.0.0.1")==True
    assert validate("124.0.0.1")==True
if __name__=="__main__":
    main()