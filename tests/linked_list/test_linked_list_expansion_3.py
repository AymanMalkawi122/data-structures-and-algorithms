import pytest
from solutions.linked_list_expansion_3.linked_list import (linked_list)



def test_initial():
    pass

def test_list1_empty():
    llist1 = linked_list()
    llist2 = linked_list()
    llist2.insert([1, 2, 3, 4])
    
    acutal = str(linked_list.zipLists(llist1, llist2))
    expected = str(llist2)
    assert acutal == expected

def test_list2_empty():
    llist1 = linked_list()
    llist2 = linked_list()
    llist1.insert([1, 2, 3, 4])
    
    acutal = str(linked_list.zipLists(llist1, llist2))
    expected = str(llist1)
    assert acutal == expected

def test_both_have_one_node():
    llist1 = linked_list()
    llist1.insert(1000)
    llist2 = linked_list()
    llist2.insert(2000)
    
    acutal = str(linked_list.zipLists(llist1, llist2))
    expected = "{ 1000 } -> { 2000 } -> NULL"
    assert acutal == expected

def test_list1_has_one_node():
    llist1 = linked_list()
    llist1.insert(1000)
    llist2 = linked_list()
    llist2.insert([1, 2, 3, 4])
    
    acutal = str(linked_list.zipLists(llist1, llist2))
    expected = "{ 1000 } -> { 4 } -> { 3 } -> { 2 } -> { 1 } -> NULL"
    assert acutal == expected

def test_list2_has_one_node():
    llist1 = linked_list()
    llist1.insert([1, 2, 3, 4])
    llist2 = linked_list()
    llist2.insert(1000)
    
    acutal = str(linked_list.zipLists(llist1, llist2))
    expected = "{ 4 } -> { 1000 } -> { 3 } -> { 2 } -> { 1 } -> NULL"
    assert acutal == expected

def test_same_length():
    llist1 = linked_list()
    llist1.insert([7, 5, 3, 1])
    llist2 = linked_list()
    llist2.insert([8, 6, 4, 2])
    
    acutal = str(linked_list.zipLists(llist1, llist2))
    expected = "{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> { 6 } -> { 7 } -> { 8 } -> NULL"
    assert acutal == expected
