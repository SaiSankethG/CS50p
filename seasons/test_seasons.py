from seasons.seasons import convert
import pytest

def main():
    test_check_minutes()

def test_check_minutes():
    assert convert("2003-09-01")=="ten million, one hundred forty thousand, four hundred eighty minutes"
    # with pytest.raise(ValueError):
    #     convert()
    assert convert("")

if __name__=="__main__":
    main()

