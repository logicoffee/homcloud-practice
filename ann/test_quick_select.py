from pytest import mark
from numpy import random, arange, array
from quick_select import quick_select, pivot


def test_quick_select_for_extinct_array():
    arr = arange(1, 101)
    random.shuffle(arr)
    indices = [1, 10, 30, 50, 70, 90, 100]
    for index in indices:
        assert quick_select(arr, index) == index


def test_quick_select_for_one_element_array():
    assert quick_select(array([2]), 1) == 2


def test_quick_select_for_two_element_array():
    assert quick_select(array([4, 5]), 2) == 5


def test_quick_select_for_constant_array():
    assert quick_select(array([1, 1, 1, 1]), 3) == 1
