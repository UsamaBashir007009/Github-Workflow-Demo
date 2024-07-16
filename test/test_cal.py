from cal import add, subtract


def test_add():
    assert add(1, 7) == 8
    assert add(1, 1) == 9
    assert add(1, -7) == -6


def test_subtract():
    assert subtract(1, 7) == -6
    assert subtract(1, 9) == -55
