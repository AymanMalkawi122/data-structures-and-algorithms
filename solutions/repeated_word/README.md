# hashmap repeated word

## Task: Write a function called repeated word that finds the first word to occur more than once in a stringimplement a linked list data structure

## 1. Whiteboard Process

![image](./assets/Screenshot%202023-07-29%20210107.png)

## 2. Approach & Efficiency

### Approach

The repeated_word function aims to find the first repeated word in the given input_string. It does so by using a Hashtable (implemented in the Hashtable class) to store each word encountered while traversing through the input string. As soon as a repeated word is found, the function returns that word; otherwise, it returns None.

### Efficiency

***Time Complexity***: The time complexity of the repeated_word function mainly depends on the hashtable operations. The insertion and lookup operations in the hashtable generally have an average case time complexity of O(1). Therefore, the overall time complexity of the function is O(n), where n is the number of words in the input string.

***Space Complexity***: The space complexity is O(m), where m is the number of unique words in the input string. In the worst case, where all words are unique, the space complexity will be O(n).

## 3. Solution

The solution provided uses a custom Hashtable class to efficiently store and look up words encountered in the input string. The input string is first converted to lowercase to ensure that the function is case-insensitive. Then, the input string is split into individual words. As the words are processed, they are inserted into the hashtable. If a word is found to be already present in the hashtable, it means it is a repeated word, and the function returns that word. If no repeated word is found during the traversal, the function returns None. The hashtable effectively keeps track of the unique words encountered so far, allowing the function to quickly identify repeated words and return the result.
