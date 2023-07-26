class Node:
    def __init__(self, key, value):
        """
        Initialize a new node with a key-value pair.

        Args:
            key: The key for the node.
            value: The value associated with the key.
        """
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None

    def append(self, key, value):
        """
        Append a new node with the given key-value pair to the end of the linked list.

        Args:
            key: The key for the new node.
            value: The value associated with the key.
        """
        new_node = Node(key, value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


class Hashtable:
    def __init__(self, size=100):
        """
        Initialize a new hash table with the given size.

        Args:
            size: The size of the hash table (number of buckets).
        """
        self.size = size
        self.buckets = [LinkedList() for temp in range(self.size)]

    def hash(self, key):
        """
        Hash the given key to an index in the hash table.

        Args:
            key: The key to be hashed.

        Returns:
            int: The index in the hash table where the key-value pair will be stored.
        """
        key = str(key)
        return sum(ord(char) for char in key) % self.size

    def set(self, key, value):
        """
        Set a key-value pair in the hash table.

        Args:
            key: The key for the key-value pair.
            value: The value associated with the key.
        """
        index = self.hash(key)
        bucket = self.buckets[index]
        current = bucket.head
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next
        bucket.append(key, value)

    def get(self, key):
        """
        Get the value associated with the given key from the hash table.

        Args:
            key: The key for which the value needs to be retrieved.

        Returns:
            Any: The value associated with the key, or None if the key is not found.
        """
        index = self.hash(key)
        bucket = self.buckets[index]
        current = bucket.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def has(self, key):
        """
        Check if the hash table contains the given key.

        Args:
            key: The key to be checked.

        Returns:
            bool: True if the key is present in the hash table, False otherwise.
        """
        if self.get(key):
            return True
        return False

    def keys(self):
        """
        Get a list of all the keys in the hash table.

        Returns:
            List: A list containing all the keys in the hash table.
        """
        keys = set()
        for bucket in self.buckets:
            current = bucket.head
            while current:
                keys.add(current.key)
                current = current.next
        return list(keys)