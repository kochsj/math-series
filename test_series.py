from series import fibonacci, lucas

def test_one():
    expected = 3
    actual = fibonacci(4)
    assert actual == expected
def test_two():
    expected = 13
    actual = fibonacci(7)
    assert actual == expected

def test_three():
    expected = 144
    actual = fibonacci(12)
    assert actual == expected

def test_four():
    expected = 29
    actual = lucas(7)
    assert actual == expected
