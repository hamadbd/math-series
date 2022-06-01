import pytest
from math_series.series import fibonacci, lucas, sum_series


# fibonacci tests.
def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert expected == actual


def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert expected == actual

def test_fibonacci_negative():
    actual = fibonacci(-1)
    expected = 'ERROR , umber below zero'
    assert actual == expected


def test_fibonacci_strings():
    actual = fibonacci("Hello")
    expected = 'Inserted data is not a number ..'
    assert actual == expected
# lucas.
def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_seven():
    actual = lucas(7)
    expected = 29
    assert actual == expected

def test_lucas_negative():
    actual = lucas(-1)
    expected = 'Inserted data is below zero ..'
    assert actual == expected

def test_lucas_strings():
    actual = fibonacci("Hello")
    expected = 'Inserted data is not a number ..'
    assert actual == expected

# sum_series tests
def test_sum_series_one():
    actual = sum_series(1)
    expected = 1
    assert actual == expected


def test_sum_series_two():
    actual = sum_series(2)
    expected = 1
    assert actual == expected


def test_sum_series_six():
    actual = sum_series(6)
    expected = 8
    assert actual == expected

