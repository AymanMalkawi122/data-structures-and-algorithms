import pytest
from solutions.sorting.insertion.insertion import insertion_sort

def test_sorting_empty_list():
    arr = []
    expected = []
    insertion_sort(arr)
    assert arr == expected

def test_sorting_sorted_list():
    arr = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    insertion_sort(arr)
    assert arr == expected

def test_sorting_reverse_list():
    arr = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    insertion_sort(arr)
    assert arr == expected

def test_sorting_random_list():
    arr = [3, 5, 1, 4, 2]
    expected = [1, 2, 3, 4, 5]
    insertion_sort(arr)
    assert arr == expected