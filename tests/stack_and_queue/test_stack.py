import pytest
from solutions.stack_and_queue.stack import (Stack)

@pytest.fixture
def stack():
   stack = Stack()
   stack.push([1, 2, 3, 4])
   return stack

def test_initial():
    pass

def test_stack_is_empty():
    stack = Stack()

    acutal = stack.is_empty()
    expected = True
    assert acutal == expected

    stack.push(1)

    acutal = stack.is_empty()
    expected = False
    assert acutal == expected

def test_get_peek_on_empty():
    stack = Stack()
    with pytest.raises(Exception):
        stack.peek()

def test_pop_on_empty():
    stack = Stack()
    with pytest.raises(Exception):
        stack.pop()

def test_push_single():
    stack = Stack()
    stack.push(1)
    acutal = stack.peek()
    expected = 1
    assert acutal == expected

def test_push_multiple(stack):
    acutal = stack.peek()
    expected = 4
    assert acutal == expected

def test_pop(stack):
    stack.pop()
    acutal = stack.peek()
    expected = 3
    assert acutal == expected

def test_pop_untill_empty(stack):
    i = 0
    while not stack.is_empty():
        i += 1
        stack.pop()
    
    assert i == 4 
    assert stack.is_empty() == True 
