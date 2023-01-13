from seasons import convert
import pytest

def main():
    test_check_minutes()

def test_check_minutes():
    assert convert("2003-09-01")=="ten million, one hundred forty thousand, four hundred eighty minutes"
    # with pytest.raise(ValueError):
    #     convert()
    assert convert("2021-12-12")=="five hundred twenty-five thousand, six hundred minutes"
    assert convert(")

if __name__=="__main__":
    main()

