# left join

## Task: implement queue using stack data structure

## 1. Whiteboard Process

![image](./assets/Screenshot%202023-08-01%20025722.png)

## 2. Approach & Efficiency

### Approach

* The left_join function aims to perform a left join operation on two hashmaps synonyms and antonyms. It combines the keys and corresponding values from the synonyms hashmap.

* If a key is present in the synonyms hashmap but not in the antonyms hashmap, it appends the corresponding value as "NULL." If the key is present in both hashmaps, it appends both corresponding values to the result.

### Efficiency

***Time Complexity***: The time complexity of the left_join function is O(n) because iterating through all the keys in the synonyms hashmap takes linear time.

***Space Complexity***: The space complexity is also O(n) because the left_join_result list stores the joined results, and its size depends on the number of keys in the synonyms hashmap.

## 3. Solution

* Create an empty list left_join_result to store the results of the left join operation.

* Iterate through the keys in the synonyms hashmap using the keys method.

* For each key, get the corresponding synonym value from the synonyms hashmap using the get method.

* Get the corresponding antonym value from the antonyms hashmap using the same key.

* Check if the synonym_value is None (i.e., the key is not present in the synonyms hashmap). If it is None, set synonym_value to "NULL".

* Check if the antonym_value is None (i.e., the key is not present in the antonyms hashmap). If it is None, set antonym_value to "NULL".

* Append the key, synonym_value, and antonym_value as a list to left_join_result.

* sAfter iterating through all keys, return left_join_result.
