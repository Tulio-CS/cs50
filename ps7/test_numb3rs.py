from numb3rs import validate


def test_ip():
    assert validate("1.2.3.4") == True
    assert validate("01.102.103.104") == True
    assert validate("255.255.255.255") == True
    assert validate("-255.255.255.255") == False
    assert validate("256.275.275.255") == False
    assert validate("255.256.255.256") == False
    assert validate("255.255.255") == False
    assert validate("255.255.255.255.255") == False
    assert validate("cat") == False

