
import pytest
from solutions.linked_list_expansion_1.linked_list import (linked_list)

def test_initial():
    pass

def test_list_append():
    list = linked_list()
    list.insert([1, 2, 3])

    list.append(4)
    actual = str(list)
    expected = "{ 3 } -> { 2 } -> { 1 } -> { 4 } -> NULL"
    assert actual == expected
    
def test_insert_before_1():
    list = linked_list()
    list.insert([1, 2, 3]) 
    with pytest.raises(Exception):
        list.insert_before(4, 10)

def test_insert_before_2():
    list = linked_list()
    list.insert([1, 2, 3])

    list.insert_before(3, 10)
    actual = str(list)
    expected = "{ 10 } -> { 3 } -> { 2 } -> { 1 } -> NULL"
    assert actual == expected

def test_insert_before_3():
    list = linked_list()
    list.insert([1, 2, 3])

    list.insert_before(2, [10, 11, 12])
    actual = str(list)
    expected = "{ 3 } -> { 12 } -> { 11 } -> { 10 } -> { 2 } -> { 1 } -> NULL"
    assert actual == expected
    
def test_insert_after_1():
    list = linked_list()
    list.insert([1, 2, 3])

    with pytest.raises(Exception):
        list.insert_after(4, 10)

def test_insert_after_2():
    list = linked_list()
    list.insert([1, 2, 3])
    
    list.insert_after(3, 10)
    actual = str(list)
    expected = "{ 3 } -> { 10 } -> { 2 } -> { 1 } -> NULL"
    assert actual == expected
    
def test_insert_after_3():
    list = linked_list()
    list.insert([1, 2, 3])
    
    list.insert_after(3, [10, 11])
    actual = str(list)
    expected = "{ 3 } -> { 11 } -> { 10 } -> { 2 } -> { 1 } -> NULL"
    assert actual == expected
