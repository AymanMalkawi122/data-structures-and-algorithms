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

    def __insert_single(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, data):
        if hasattr(data, '__len__'):
            for element in data:
                new_node = Node(element)
                new_node.next = self.head
                self.head = new_node
        else:
            self.__insert_single(data)


    def includes(self, value):
        current_node = self.head
        while current_node != None:
            if current_node.data == value:
                return True
            current_node = current_node.next
        return False
    
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
insert(data): Inserts multiple nodes with the given data at the beginning of the linked list.
includes(value): Searches the linked list for a node with the given value and returns True if found, otherwise False.
str(): Returns a string representation of the linked list.
"""


