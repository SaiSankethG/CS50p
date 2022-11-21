from twttr.twttr import shorten

def test_uppercase():
    assert shorten('LONG')=='LNG'
    assert shorten('TWITTER')=='TWTTR'

def test_number():
    assert shorten('1234')=='1234'

def test_lowercase():
    assert shorten('twitter')=='twttr'

