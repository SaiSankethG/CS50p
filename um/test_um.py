from um.um import count
import sys

def main():
#     test_value()
#     test_zero()
    test_upper_lower_case()
    test_word_with_um()
    test_by_space()
    sys.exit(0)

def test_upper_lower_case():
    assert count("Um , thanks for the album")==1
    assert count("Um , thanks , um...")==2

def test_word_with_um():
    assert count("yummy")==0

def test_by_space():
    assert count("Hello um world")==1
# def test_value():
#     assert count("hello, um, world , um")==2
#     assert count("um")==1
#     assert count("um?")==1
#     assert count("Um, thanks for the album")==1

# def test_zero():
#     assert count("hello, world")==0

if __name__=="__main__":
    main()