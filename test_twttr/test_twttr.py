from twttr.twttr import shorten
def main():
    test_uppercase()
    test_number()
    test_lowercase()

def test_uppercase():
    assert shorten('LONG')=='LNG'
    assert shorten('TWITTER')=='TWTTR'

def test_number():
    assert shorten('1234')=='1234'

def test_lowercase():
    assert shorten('twitter')=='twttr'

def test_punctuation():
    assert shorten('?/!.,')=='?/!.,'

if __name__=="__main__":
    main()

