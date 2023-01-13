from fuel import convert, gauge
import pytest

def test_convert():
    assert convert('1/10')==0.1 and gauge(0.1)=='10%'
    assert convert('1/1')==1 and gauge(1)=='F'
    assert convert('1/100')==0.01 and gauge(0.01)=='E'
    assert convert('1')==None

# def test_zerodivison():
#     with pytest.raises(ZeroDivisionError):
#         convert('1/0')

# def test_value():
#     with pytest.raises(ValueError):
#         convert('cat/dog')




