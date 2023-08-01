import pytest
from solutions.hash_tables.solution import Hashtable
from solutions.left_join.solution import left_join

@pytest.fixture
def synonyms_hashtable():
    synonyms = Hashtable()
    synonyms.set("diligent", "employed")
    synonyms.set("fond", "enamored")
    synonyms.set("guide", "usher")
    synonyms.set("outfit", "garb")
    synonyms.set("wrath", "anger")
    return synonyms

@pytest.fixture
def antonyms_hashtable():
    antonyms = Hashtable()
    antonyms.set("diligent", "idle")
    antonyms.set("fond", "averse")
    antonyms.set("guide", "follow")
    antonyms.set("flow", "jam")
    antonyms.set("wrath", "delight")
    return antonyms


def test_left_join(synonyms_hashtable, antonyms_hashtable):
    expected_output = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", "NULL"],
        ["wrath", "anger", "delight"]
    ]
    assert sorted(left_join(synonyms_hashtable, antonyms_hashtable)) == sorted(expected_output)


def test_left_join_matching_keys(synonyms_hashtable, antonyms_hashtable):
    synonyms_hashtable.set("happy", "joyful")
    antonyms_hashtable.set("happy", "sad")

    expected_output = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", "NULL"],
        ["wrath", "anger", "delight"],
        ["happy", "joyful", "sad"]
    ]
    assert sorted(left_join(synonyms_hashtable, antonyms_hashtable)) == sorted(expected_output)


def test_left_join_extra_synonyms_keys(synonyms_hashtable, antonyms_hashtable):
    synonyms_hashtable.set("amazing", "incredible")
    synonyms_hashtable.set("brave", "courageous")

    expected_output = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", "NULL"],
        ["wrath", "anger", "delight"],
        ["amazing", "incredible", "NULL"],
        ["brave", "courageous", "NULL"]
    ]
    assert sorted(left_join(synonyms_hashtable, antonyms_hashtable)) == sorted(expected_output)


def test_left_join_empty_hashtables():
    synonyms_hashtable = Hashtable()
    antonyms_hashtable = Hashtable()

    assert sorted(left_join(synonyms_hashtable, antonyms_hashtable)) == sorted([])


def test_left_join_empty_synonyms(synonyms_hashtable):
    antonyms_hashtable = Hashtable()

    expected_output = [
        ["diligent", "employed", "NULL"],
        ["fond", "enamored", "NULL"],
        ["guide", "usher", "NULL"],
        ["outfit", "garb", "NULL"],
        ["wrath", "anger", "NULL"]
    ]
    assert sorted(left_join(synonyms_hashtable, antonyms_hashtable)) == sorted(expected_output)


def test_left_join_empty_antonyms(antonyms_hashtable):
    synonyms_hashtable = Hashtable()

    expected_output = []
    assert sorted(left_join(synonyms_hashtable, antonyms_hashtable)) == sorted(expected_output)