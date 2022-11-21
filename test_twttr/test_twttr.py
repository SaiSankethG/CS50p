import twttr.twttr as shorten

def test_uppercase():
    assert shorten('LONG')=='LNG'
    assert shorten('TWITTER')=='TWTTR'

