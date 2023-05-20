import pytest
from solutions.linked_list_expansion_2.linked_list import (linked_list)


@pytest.fixture
def test_list():
   llist = linked_list()
   llist.insert([1, 2, 3, 4])
   return llist

def test_initial():
    pass

def test_list_append(test_list):
    test_list.append(5)
    actual = str(test_list)
    expected = "{ 4 } -> { 3 } -> { 2 } -> { 1 } -> { 5 } -> NULL"
    assert actual == expected
    
def test_insert_before_1(test_list):
    with pytest.raises(Exception):
        test_list.insert_before(5, 10)

def test_insert_before_2(test_list):
    test_list.insert_before(4, 10)
    actual = str(test_list)
    expected = "{ 10 } -> { 4 } -> { 3 } -> { 2 } -> { 1 } -> NULL"
    assert actual == expected

def test_insert_before_3(test_list):
    test_list.insert_before(1, [10, 11, 12])
    actual = str(test_list)
    expected = "{ 4 } -> { 3 } -> { 2 } -> { 12 } -> { 11 } -> { 10 } -> { 1 } -> NULL"
    assert actual == expected
    
def test_insert_after_1(test_list):
    with pytest.raises(Exception):
        test_list.insert_after(5, 10)

def test_insert_after_2(test_list):
    
    test_list.insert_after(4, 10)
    actual = str(test_list)
    expected = "{ 4 } -> { 10 } -> { 3 } -> { 2 } -> { 1 } -> NULL"
    assert actual == expected
    
def test_insert_after_3(test_list):
    
    test_list.insert_after(1, [10, 11])
    actual = str(test_list)
    expected = "{ 4 } -> { 3 } -> { 2 } -> { 1 } -> { 11 } -> { 10 } -> NULL"
    assert actual == expected
