import pytest
from app.tests.add import add


# abc



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

