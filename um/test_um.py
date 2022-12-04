from um.um import count

def main():
    test_value()
    test_zero()

def test_value():
    assert count("hello, um, world , um")==2
    assert count("um")==1
    assert count("um?")==1
    assert count("Um, thanks for the album")==1

def test_zero():
    assert count("hello, world")==0

if __name__=="__main__":
    main()