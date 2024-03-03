from um import count

def test_count():
    assert count("um") == 1
    assert count("um, yummy, um") == 2
    assert count("hello, world") == 0
    assert count("hello, um, world") == 1
    assert count("Um!") == 1


