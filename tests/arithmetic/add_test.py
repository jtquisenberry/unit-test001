from app.arithmetic.add import *


def add_test():
    """
    Demonstrates a test named as *_test. This test is expected to pass.
    """
    a = 1
    b = 2
    actual = add(a, b)
    expected = 3
    assert actual == expected

def test_add():
    """
    Demonstrates a test named as test_*. This test is expected to pass.
    """
    a = 1
    b = 2
    actual = add(a, b)
    expected = 3
    assert actual == expected

def bad_add_test():
    """
    Tests a bad implementation of addition.
    """
    a = 1
    b = 2
    actual = bad_add(a, b)
    expected = 3
    assert actual == expected

