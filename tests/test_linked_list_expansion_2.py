
import pytest
from solutions.linked_list_expansion_2.linked_list import (linked_list)


@pytest.fixture
def test_list():
   llist = linked_list()
   llist.insert([1, 2, 3, 4])
   return llist

def test_initial():
    pass
def 
def test_k_greater_than_length(test_list):
    with pytest.raises(Exception):
        test_list.insert_after(5, 10)
    
def test_insert_after_3(test_list):
    
    test_list.insert_after(1, [10, 11])
    actual = str(test_list)
    expected = "{ 4 } -> { 3 } -> { 2 } -> { 1 } -> { 11 } -> { 10 } -> NULL"
    assert actual == expected
