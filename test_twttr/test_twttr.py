from twttr import shorten

def test_shorten():
    assert shorten(sai_sanketh)=="s_snkth"

def test_twttr():
    assert shorten(twitter)==