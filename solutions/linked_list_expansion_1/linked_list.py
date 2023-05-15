class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  
  
"""
A class that represents a single node in a linked list.

Attributes:
data (any): The data value of the node.
next (Node): The reference to the next node in the linked list.
"""

class linked_list:
    def __init__(self): 
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_all(self, data):
        for element in data:
            new_node = Node(element)
            new_node.next = self.head
            self.head = new_node

    def includes(self, value):
        current_node = self.head
        while current_node != None:
            if current_node.data == value:
                return True
            current_node = current_node.next
        return False
    
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return
        current_node = self.head
        while(current_node != None):
            if current_node.next == None:
                current_node.next = new_node
                return
            current_node = current_node.next

    def insert_before(value, new_value):
        new_node = Node(value)

    def insert_after(value, new_value):
        new_node = Node(value)

    def __str__(self):
        result = ""

        current_node = self.head
        while current_node != None:
            result += f"{{ {current_node.data} }} -> "
            current_node = current_node.next
        result += "NULL"

        return result
       
"""
A class that represents a linked list data structure.

Attributes:
head : The reference to the head node of the linked list.

Methods:
insert(data): Inserts a new node with the given data at the beginning of the linked list.
insert_all(data): Inserts multiple nodes with the given data at the beginning of the linked list.
includes(value): Searches the linked list for a node with the given value and returns True if found, otherwise False.
str(): Returns a string representation of the linked list.
"""


