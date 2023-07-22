# Hash Table

## Task: Implement a Hashtable Class

## Approach & Efficiency

### Approach

1. The Hashtable class is implemented with a fixed-size array of buckets. Each bucket is a linked list to handle collisions.
2. A simple hash function is used to convert the key into an index to determine the bucket for the key-value pair.
3. The set method first calculates the index using the hash function and then traverses the linked list in the bucket to find if the key already exists. If found, it updates the value; otherwise, it appends a new node to the linked list.
4. The get method uses the hash function to find the bucket and then traverses the linked list to locate the key and return its value.
5. The has method follows a similar approach as get, but it returns a boolean value indicating if the key exists in the hashtable.
6. The keys method iterates through all buckets, collects unique keys in a set, and returns the keys as a list.

7. Hash Function:

    The simple hash function uses the sum of the ASCII values of characters in the key and then calculates the modulo with the size of the hashtable to get an index within the range of buckets.

### Efficiency

* **Time complexity**: set, get, has, and keys methods: In the worst case, when there are many collisions and all keys hash to the same index, the time complexity of these methods can be O(n), where n is the number of key-value pairs in the hashtable. On average, when there are fewer collisions, the time complexity approaches O(1).
Hash Function: The time complexity of the hash function is O(k), where k is the length of the key. Since the keys' length is usually small and constant, the hash function can be considered as O(1).
Space Complexity:

* **Space complexity**: The space complexity of the Hashtable is O(m + n), where m is the size of the hashtable (number of buckets), and n is the number of key-value pairs in the hashtable. In our implementation, the size is fixed at 100 (m = 100), and the space used for each key-value pair is constant (O(1)).
The space complexity of the hash function is also O(1) since it uses a fixed number of operations and does not depend on the input size.

## 3. Solution

this implementation of the Hashtable class is efficient for small to moderate-sized datasets and provides constant-time lookups in the average case when there are fewer collisions. However, for larger datasets and potential high collision rates, more advanced hash table implementations, like chaining with balanced trees or open addressing, may offer better performance.
