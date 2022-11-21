import sys
sys.path.insert('../test_twttr/test_twttr.py')
from twttr import shorten

def test_shorten():
    assert shorten(word)=="wrd"

def test_long():
    assert shorten(Long)=="Lng"
