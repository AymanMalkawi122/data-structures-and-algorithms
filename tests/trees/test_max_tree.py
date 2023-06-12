import pytest
from solutions.trees.tree import BinaryTree, Node

def test_initial():
    pass

def test_max_empty():
    tree = BinaryTree()
    assert tree.max_node() == None


def test_max_single_root():
    tree = BinaryTree()
    root_node = Node(1)
    tree.root = root_node
    assert tree.max_node() == 1

def test_max_root_left_right():
    tree = BinaryTree()
    root_node = Node(-10)
    root_node.left = Node(-5)
    root_node.right = Node(-1)
    tree.root = root_node
    assert tree.max_node() == -1