import pytest
from solutions.repeated_word.solution import repeated_word

def test_repeated_word():
    input_string = "Once upon a time, there was a brave knight. The brave knight fought a dragon."
    assert repeated_word(input_string) == "a"


def test_no_repeated_word():
    input_string = "A quick brown fox jumps over the lazy dog."
    assert repeated_word(input_string) is None


def test_case_insensitive():
    input_string = "Once once"
    assert repeated_word(input_string) == "once"


def test_compound_words():
    input_string = "HelloWorld HelloWorld is a popular phrase in programming."
    assert repeated_word(input_string) == "helloworld"


def test_empty_string():
    input_string = ""
    assert repeated_word(input_string) is None