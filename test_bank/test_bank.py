from bank.bank import value

def main():
    test_0
    test_20
    test_100


def test_0():
    assert value('hello')=='$0'
    assert value('HELLO')=='$0'
def test_20():
    assert value('hi')=='$20'
    assert value('HI')=='$20'
def test_100():
    assert value('wtf')=='$100'
    assert value('what the fuck')=='$100'

if __name__=="__main__":
    main()

