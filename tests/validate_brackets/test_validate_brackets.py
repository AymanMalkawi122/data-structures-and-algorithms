import pytest
from solutions.stack_queue_brackets.brackets import validate_brackets

def test_initial():
    pass

def test_empty_string():
    acutal = validate_brackets("")
    expected = True
    assert acutal == expected

def test_valid_string_1():
    acutal = validate_brackets("()")
    expected = True
    assert acutal == expected

def test_valid_string_2():
    acutal = validate_brackets("{}(){}")
    expected = True
    assert acutal == expected

def test_valid_string_3():
    acutal = validate_brackets("()[[Extra Characters]]")
    expected = True
    assert acutal == expected

def test_valid_string_4():
    acutal = validate_brackets("(){}[[]]")
    expected = True
    assert acutal == expected

def test_valid_string_5():
    acutal = validate_brackets("{}{Code}[Fellows](())")
    expected = True
    assert acutal == expected	


def test_invalid_string_1():
    acutal = validate_brackets("[({}]")
    expected = False
    assert acutal == expected

def test_invalid_string_2():
    acutal = validate_brackets("(](")
    expected = False
    assert acutal == expected

def test_invalid_string_3():
    acutal = validate_brackets("{(})")
    expected = False
    assert acutal == expected

	
# 	
# 	
# 