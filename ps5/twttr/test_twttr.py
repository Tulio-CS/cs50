from twttr import shorten


def test_shorten():
    assert shorten("Tulio") == "Tl"
    assert shorten("hello world") == "hll wrld"
    assert shorten("HELLO WORLD") == "HLL WRLD"
    assert shorten("CS50") == "CS50"
    assert shorten("Ibtech !") == "btch !"


