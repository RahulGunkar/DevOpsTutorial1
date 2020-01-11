import pytest

def func(x):
    return x + 1


def test_sample1():
    assert func(4) == 5

def test_sample2():
    assert func(5) == 6

def test_sample3():
    assert func(6) == 7

def test_sample4():
    assert func(7) == 8
