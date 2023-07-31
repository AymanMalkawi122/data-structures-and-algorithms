from solutions.hash_tables.solution import Hashtable
def traverse(node, result):
  """
    Perform a pre-order traversal of a binary tree starting from the given 'node'.

    Args:
        node (TreeNode): The starting node of the binary tree.
        result (list): A list to store the values obtained from the traversal.

    Returns:
        None
  """
  if node:
    result.append(node.value)
    traverse(node.left, result)
    traverse(node.right, result)
   

def tree_intersection(tree1, tree2):
    """
    Find the common values that occur in both binary trees 'tree1' and 'tree2'.

    Args:
        tree1 (BinaryTree): The first binary tree.
        tree2 (BinaryTree): The second binary tree.

    Returns:
        list: A list containing values common to both binary trees.
    """
    repetitions = Hashtable(100)
    tree_values = []
    traverse(tree1.root, tree_values)

    for value in tree_values:
      repetitions.set(value, 1)

    tree_values = []
    traverse(tree2.root, tree_values)

    for value in tree_values:
      if repetitions.get(value):
        repetitions.set(value, 2)
      else:
        repetitions.set(value, 1)

    result = []
    keys = repetitions.keys()

    for key in keys:
      if repetitions.get(key) == 2:
        result.append(key)
    return result