import pytest
from solutions.stack_queue_pseudo.queue import (QueuePseudo)

@pytest.fixture
def queue():
   queue = QueuePseudo()
   queue.enqueue([1, 2, 3, 4])
   return queue

def test_initial():
    pass

def instantiate_empty_queue():
    queue = QueuePseudo()

    acutal = queue.is_empty()
    expected = True
    assert acutal == expected

def test_queue_isnt_empty():
    stack = QueuePseudo()
    stack.enqueue(1)

    acutal = stack.is_empty()
    expected = False
    assert acutal == expected

def test_get_peek_on_empty():
    queue = QueuePseudo()
    with pytest.raises(Exception):
        queue.peek()

def test_dequeue_on_empty():
    queue = QueuePseudo()
    with pytest.raises(Exception):
        queue.dequeue()

def test_enqueue_single():
    queue = QueuePseudo()
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

