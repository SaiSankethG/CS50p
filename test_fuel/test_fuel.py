from fuel.fuel import convert, gauge

def test_convert():
    convert(1/10)==0.1
    convert(1/1)==1
    convert(1)=="ValueError"

def test_gauge():
    gauge(0.1)==10
    gauge(1)=='E'
    