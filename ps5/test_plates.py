from plates import is_valid


def test_minmax():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("ABCDEF") == True

def test_numbers():
    assert is_valid("1ABC10") == False
    assert is_valid("ABC01") == False
    assert is_valid("123456") == False
    assert is_valid("AB1C2") == False
    assert is_valid("PL12AT") == False
    assert is_valid("ABC123") == True

def test_first_letter():
    assert is_valid("1") == False
    assert is_valid("11") == False
    assert is_valid("TU") == True

def test_symbols():
    assert is_valid("ABC12;") == False
    assert  is_valid(";:.ABC") == False
    
