import pytest
from solutions.trees.tree import BinaryTree, Node

def test_initial():
    pass

def test_max_root_is_None():
    tree = BinaryTree()
    root_node = None
    tree.root = root_node
    assert tree.max_node() == None


def test_max_root_no_children():
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

def test_max_complex_tree():
    tree = BinaryTree()
    root_node = Node(10)
    root_node.left = Node(5)
    root_node.right = Node(1)
    root_node.right.right = Node(20)
    root_node.right.right = Node(30)
    root_node.left.right = Node(15)
    root_node.left.right = Node(16)
    tree.root = root_node
    assert tree.max_node() == 30
