import pytest
from solutions.stack_queue_animal_shelter.animal_shelter import (AnimalShelter, Animal)

@pytest.fixture
def empty():
    empty = AnimalShelter()
    return empty

def test_initial():
    pass

def instantiate_empty_shelter(empty):
    acutal = empty.dequeue("dog")
    expected = None
    assert acutal == expected
    acutal = empty.dequeue("cat")
    expected = None
    assert acutal == expected

def test_shelter_isnt_empty(empty):
    shelter = empty
    shelter.enqueue(Animal("dog", "Buddy"))

    acutal = shelter.dequeue("dog").name
    expected = "Buddy"
    assert acutal == expected

def test_cats_without_dogs(empty):
    shelter = empty
    shelter.enqueue(Animal("cat", "Cat Name 1"))
    shelter.enqueue(Animal("cat", "Cat Name 2"))
    shelter.enqueue(Animal("cat", "Cat Name 3"))

    acutal = shelter.dequeue("dog")
    expected = None
    assert acutal == expected

    acutal = shelter.dequeue("cat").name
    expected = "Cat Name 1"
    assert acutal == expected

def test_dogs_without_cats(empty):
    shelter = empty
    shelter.enqueue(Animal("dog", "Dog Name 1"))
    shelter.enqueue(Animal("dog", "Dog Name 2"))
    shelter.enqueue(Animal("dog", "Dog Name 3"))

    acutal = shelter.dequeue("cat")
    expected = None
    assert acutal == expected

    acutal = shelter.dequeue("dog").name
    expected = "Dog Name 1"
    assert acutal == expected


def test_invalid_animal_type(empty):
    shelter = empty
    shelter.enqueue(Animal("dog", "Dog Name 1"))
    shelter.enqueue(Animal("cat", "Cat Name 1"))
    shelter.enqueue(Animal("dog", "Dog Name 2"))

    acutal = shelter.dequeue("bird")
    expected = None
    assert acutal == expected

def test_correct_animal_order(empty):
    shelter = empty
    shelter.enqueue(Animal("dog", "Dog Name 1"))
    shelter.enqueue(Animal("cat", "Cat Name 1"))
    shelter.enqueue(Animal("dog", "Dog Name 2"))
    shelter.enqueue(Animal("cat", "Cat Name 2"))

    acutal = shelter.dequeue("cat").name
    expected = "Cat Name 1"
    assert acutal == expected

    acutal = shelter.dequeue("cat").name
    expected = "Cat Name 2"
    assert acutal == expected

    acutal = shelter.dequeue("cat")
    expected = None
    assert acutal == expected

    acutal = shelter.dequeue("dog").name
    expected = "Dog Name 1"
    assert acutal == expected

    acutal = shelter.dequeue("dog").name
    expected = "Dog Name 2"
    assert acutal == expected

    acutal = shelter.dequeue("dog")
    expected = None
    assert acutal == expected
