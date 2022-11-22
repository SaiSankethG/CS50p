from fuel.fuel import convert, gauge

def test_convert():
    assert convert('1/10')==0.1
    assert convert('1/1')==1
    assert convert('1')=="ValueError"

def test_gauge():
    assert gauge(0.1)==10
    assert gauge(1)=='E'
