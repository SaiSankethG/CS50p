from numb3rs.numb3rs import validate
import sys

def main():
    test_char()
    test_out_of_range()
    test_range()
    sys.exit(0)

def test_char():
    assert validate(r"cat")==False
    assert validate(r"dog")==False
def test_out_of_range():
    assert validate(r"277.0.0.1")==False
    assert validate(r"255.255.255.288")==False
    assert validate(r"127.0.0.1111")==False
def test_range():
    assert validate(r"127.0.0.1")==True
    assert validate(r"124.0.0.1")==True
if __name__=="__main__":
    main()