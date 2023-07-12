import pytest
from solutions.sorting.merge.merge import merge_sort

def test_empty_array():
        arr = []
        expected_result = []
        arr = merge_sort(arr)
        assert(arr, expected_result)

def test_sorted_array():
    arr = [1, 2, 3, 4, 5]
    expected_result = [1, 2, 3, 4, 5]
    arr = merge_sort(arr)
    assert(arr, expected_result)

def test_reverse_sorted_array():
    arr = [5, 4, 3, 2, 1]
    expected_result = [1, 2, 3, 4, 5]
    arr = merge_sort(arr)
    assert(arr, expected_result)

def test_random_array():
    arr = [9, 2, 7, 1, 5]
    expected_result = [1, 2, 5, 7, 9]
    arr = merge_sort(arr)
    assert(arr, expected_result)

def test_duplicate_elements():
    arr = [3, 2, 5, 2, 1]
    expected_result = [1, 2, 2, 3, 5]
    arr = merge_sort(arr)
    assert(arr, expected_result)

def test_negative_numbers():
    arr = [-5, -2, -8, -1, -3]
    expected_result = [-8, -5, -3, -2, -1]
    arr = merge_sort(arr)
    assert(arr, expected_result)

def test_already_sorted_large_array():
    arr = list(range(1000))
    expected_result = list(range(1000))
    arr = merge_sort(arr)
    assert(arr, expected_result)

def test_reverse_sorted_large_array():
    arr = list(range(1000, 0, -1))
    expected_result = list(range(1, 1001))
    arr = merge_sort(arr)
    assert(arr, expected_result)

def test_single_element_array():
    arr = [42]
    expected_result = [42]
    arr = merge_sort(arr)
    assert(arr, expected_result)

def test_duplicate_elements_large_array():
    arr = [4, 2, 5, 2, 1] * 200
    expected_result = [1, 2, 2, 4, 5] * 200
    arr = merge_sort(arr)
    assert(arr, expected_result)