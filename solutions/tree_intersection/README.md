# stack queue pseudo

## Task: Write a function called tree_intersection that takes two binary trees as parameters using your Hashmap implementation as a part of your algorithm, return a set of values found in both trees

## 1. Whiteboard Process

![image](./assets/Screenshot%202023-08-01%20022116.png)

## 2. Approach & Efficiency

### Approach

The tree_intersection function aims to find the common values that occur in both binary trees tree1 and tree2. To achieve this, we follow these steps:

1. Use a Hashtable (repetitions) to store the values from tree1 and their repetition counts.
2. Traverse tree1 using a pre-order traversal (traverse function) and populate the tree_values list with the values from tree1.
3. Iterate through the values in tree_values and set them in the repetitions Hashtable with a repetition count of 1.
4. Reset the tree_values list to prepare it for traversal of tree2.
5. Traverse tree2 using the pre-order traversal (traverse function) and update the repetition counts in the repetitions Hashtable for each value from tree2.
6. Initialize an empty list (result) to store the values common to both trees.
7. Obtain all the keys (values from the trees) present in the repetitions Hashtable using the keys method.
8. Iterate through the keys and check if the repetition count for each key is 2. If it is, append the key to the result list.
9. Return the result list, containing values common to both trees.

### Efficiency

***Space Complexity:***

auxiliary variables (such as result and keys) and the function call stack for the traverse function contribute to a constant amount of space and do not significantly affect the overall space complexity.

Therefore, the overall space complexity of the code is O(n).

***Time Complexity:***

The time complexity of the traverse function is O(n) as it performs a pre-order traversal, visiting each node once, where n is the number of nodes in the tree.

Therefore, the overall time complexity of the code is O(n) where n is the total number of nodes in both trees

## 3. Solution

* The solution uses a Hashtable to efficiently track the repetition count of values from both binary trees. By performing pre-order traversals on both trees, the solution efficiently finds the common values and returns them as the final output. The time complexity is O(n + k), where n is the total number of nodes in both trees, and k is the number of common values between the trees. The space complexity is O(n), as it mainly depends on the repetitions Hashtable and temporary lists used during traversals.
