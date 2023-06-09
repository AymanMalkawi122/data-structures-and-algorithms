import pytest

from solutions.linked_list_expansion_3.linked_list import (
    linked_list,
)

@pytest.fixture
def test_list():
   llist = linked_list()
   llist.insert([1, 2, 3, 4])
   return llist

def test_initial():
    pass

def test_list_construct():
    test_list = linked_list()
    actual = test_list.head
    expected = None
    assert actual == expected
    
def test_list_insert():
    test_list = linked_list()
    test_list.insert(5)
    actual = test_list.head.data
    expected = 5
    assert actual == expected

def test_list_insert_2(test_list):
    actual = test_list.head.data
    expected = 4
    assert actual == expected
    
def test_head_points_to_start(test_list):
    test_list.insert(9)
    actual = test_list.head.data
    expected = 9
    assert actual == expected

def test_list_includes_1(test_list):
    actual = test_list.includes(4)
    expected = True
    assert actual == expected

def test_list_includes_2(test_list):
    actual = test_list.includes(69)
    expected = False
    assert actual == expected

def test_list_str(test_list):
    actual = str(test_list)
    expected = "{ 4 } -> { 3 } -> { 2 } -> { 1 } -> NULL"
    assert actual == expected