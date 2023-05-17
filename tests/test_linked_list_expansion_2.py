
import pytest
from solutions.linked_list_expansion_2.linked_list import (linked_list)


@pytest.fixture
def test_list():
   llist = linked_list()
   llist.insert([1, 2, 3, 4])
   return llist

def test_initial():
    pass

def test_k_greater_than_length(test_list):
    with pytest.raises(Exception):
        test_list.kthFromEnd(4)

def test_k_negative(test_list):
    with pytest.raises(Exception):
        test_list.kthFromEnd(5)
     
def test_k_equal_to_length(test_list):
    acutal = test_list.kthFromEnd(3)
    expected = 4
    assert acutal == expected

def test_k_equal_to_zero(test_list):
    acutal = test_list.kthFromEnd(0)
    expected = 1
    assert acutal == expected

def test_k_in_middle(test_list):
    acutal = test_list.kthFromEnd(2)
    expected = 3
    assert acutal == expected

