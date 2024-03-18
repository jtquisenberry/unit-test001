import pytest
from tests.add import add


def add_test():
    a = 1
    b = 2
    actual = add(a, b)
    expected = 3
    print("XXXXXXXXXXXXXxxxx")
    assert actual == expected

def test_add():
    a = 1
    b = 2
    actual = add(a, b)
    expected = 3
    assert actual == expected

