from cal import add


def test_add():
    assert add(1, 7) == 8
    assert add(1, 1) == 2
    assert add(1, -7) == -6
