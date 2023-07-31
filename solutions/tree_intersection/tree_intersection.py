from solutions.hash_tables.solution import Hashtable
def traverse(node, result):
  if node:
    result.append(node.value)
    traverse(node.left, result)
    traverse(node.right, result)
    

def tree_intersection(tree1, tree2):
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