from seasons import diff_to_min

def test_diff_to_min():
    assert diff_to_min(365) == "Five hundred twenty-five thousand, six hundred minutes"
    assert diff_to_min(7282) == "Ten million, four hundred eighty-six thousand eighty minutes"
