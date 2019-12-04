from series import fibonacci, lucas

def test_one():
    expected = 'hello'
    actual = fibonacci('')
    assert actual == expected

def test_two():
    expected = 'world'
    actual = lucas('')
    assert actual == expected
