import pytest
from solutions.trees.tree import BinarySearchTree
from solutions.tree_intersection.tree_intersection import tree_intersection

def test_tree_intersection():
    tree1 = BinarySearchTree()
    tree2 = BinarySearchTree()
    common_values = [10, 20, 30, 40, 50]
    for value in common_values:
        tree1.add(value)
        tree2.add(value)

    extra_values = [60, 70, 80, 90, 100]
    for value in extra_values:
        tree2.add(value)

    expected_result = sorted(common_values)

    result = tree_intersection(tree1, tree2)

    assert sorted(result) == expected_result


def test_tree_intersection_no_common_values():
    tree1 = BinarySearchTree()
    tree2 = BinarySearchTree()
    values1 = [1, 2, 3, 4, 5]
    values2 = [6, 7, 8, 9, 10]
    for value in values1:
        tree1.add(value)
    for value in values2:
        tree2.add(value)

    expected_result = []

    result = tree_intersection(tree1, tree2)

    assert result == expected_result

def test_tree_intersection_one_empty_tree():
    tree1 = BinarySearchTree()
    tree2 = BinarySearchTree()
    values1 = [1, 2, 3, 4, 5]
    for value in values1:
        tree1.add(value)

    expected_result = []

    result = tree_intersection(tree1, tree2)

    assert result == expected_result

def test_tree_intersection_both_empty_trees():
    # Create two empty binary search trees
    tree1 = BinarySearchTree()
    tree2 = BinarySearchTree()

    # Calculate the expected result (intersection of two empty lists)
    expected_result = []

    # Call the tree_intersection function with both empty trees
    result = tree_intersection(tree1, tree2)

    # Assert that the result matches the expected_result
    assert result == expected_result