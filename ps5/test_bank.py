from bank import value

def test_value_casesensitivity():
    assert value("hello world") == 0
    assert value("Hello") == 0

def test_value_firstletter():
    assert value("hi") == 20
    assert value("Hasta la vista!") == 20

def test_value_failure():
    assert value("oi?") == 100
    assert value("1# Customer!") == 100

