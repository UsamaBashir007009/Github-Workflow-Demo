from cal import add, subtract


def test_add():
    assert add(1, 9) == 10
    assert add(1, 3) == 4
    assert add(1, -7) == -6


def test_subtract():
    assert subtract(1, 1) == 0
    assert subtract(1, 3) == -2
