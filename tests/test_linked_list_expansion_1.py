
import pytest
from solutions.linked_list_expansion_1.linked_list import (linked_list)

def test_initial():
    pass

def test_list_append():
    test_list = linked_list()
    test_list.insert_all([1, 2, 3])

    test_list.append(4)
    actual = test_list.includes(4)
    expected = True
    assert actual == expected
    
def test_insert_before_1():
    test_list = linked_list()
    test_list.insert_all([1, 2, 3])
    
    with pytest.raises(Exception):
        test_list.insert_before(4, 10)

def test_insert_before_2():
    test_list = linked_list()
    test_list.insert_all([1, 2, 3])

    test_list.insert_before(3, 10)
    actual = test_list.includes(10)
    expected = True
    assert actual == expected
    
def test_insert_after_1():
    test_list = linked_list()
    test_list.insert_all([1, 2, 3])

    with pytest.raises(Exception):
        test_list.insert_after(4, 10)

def test_insert_after_2():
    test_list = linked_list()
    test_list.insert_all([1, 2, 3])
    
    test_list.insert_after(3, 10)
    actual = test_list.includes(10)
    expected = True
    assert actual == expected
