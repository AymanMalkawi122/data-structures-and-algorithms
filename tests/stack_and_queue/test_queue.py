import pytest
from solutions.stack_and_queue.queue import (Queue)

@pytest.fixture
def queue():
   queue = Queue()
   queue.enqueue([1, 2, 3, 4])
   return queue

def test_initial():
    pass

def instantiate_empty_queue():
    queue = Queue()

    acutal = queue.is_empty()
    expected = True
    assert acutal == expected

def test_queue_isnt_empty():
    stack = Queue()
    stack.enqueue(1)

    acutal = stack.is_empty()
    expected = False
    assert acutal == expected

def test_get_peek_on_empty():
    queue = Queue()
    with pytest.raises(Exception):
        queue.peek()

def test_dequeue_on_empty():
    queue = Queue()
    with pytest.raises(Exception):
        queue.dequeue()

def test_enqueue_single():
    queue = Queue()
    queue.enqueue(1)
    acutal = queue.peek()
    expected = 1
    assert acutal == expected

def test_enqueue_multiple(queue):
    acutal = queue.peek()
    expected = 1
    assert acutal == expected

def test_dequeue(queue):
    queue.dequeue()
    acutal = queue.peek()
    expected = 2
    assert acutal == expected

def test_dequeue_untill_empty(queue):
    i = 0
    while not queue.is_empty():
        i += 1
        queue.dequeue()
    
    assert i == 4 
    assert queue.is_empty() == True 

