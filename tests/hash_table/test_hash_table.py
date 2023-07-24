import pytest
from solutions.hash_tables.solution import Hashtable


@pytest.fixture
def hashtable():
    return Hashtable()

def test_set_and_get(hashtable):
    hashtable.set("name", "John")
    assert hashtable.get("name") == "John"

def test_get_non_existent_key(hashtable):
    assert hashtable.get("invalid") is None

def test_has_key(hashtable):
    hashtable.set("name", "John")
    assert hashtable.has("name") is True
    assert hashtable.has("invalid") is False

def test_keys(hashtable):
    hashtable.set("name", "John")
    hashtable.set("age", 30)
    hashtable.set("country", "USA")
    assert set(hashtable.keys()) == {"name", "age", "country"}

def test_collision(hashtable):
    # hash(abc) = hash(cba)
    hashtable.set("abc", "red")
    hashtable.set("cba", "yellow")
    assert hashtable.get("abc") == "red"
    assert hashtable.get("cba") == "yellow"

def test_retrieve_collision_value(hashtable):
    hashtable.set("abc", "red")
    hashtable.set("cba", "yellow")
    assert hashtable.get("abc") == "red"
    assert hashtable.get("cba") == "yellow"

def test_hash_value_range(hashtable):
    key = "test_key"
    hashed_value = hashtable.hash(key)
    assert 0 <= hashed_value < hashtable.size