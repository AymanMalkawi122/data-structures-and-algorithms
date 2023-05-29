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

class Stack:
    def __init__(self): 
        self.top = None

    def __push_single(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def is_empty(self):
        return self.top == None

    def push(self, data):
        if hasattr(data, '__len__'):
            for element in data:
                new_node = Node(element)
                new_node.next = self.top
                self.top = new_node
        else:
            self.__push_single(data)

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty!")
        return self.top.data
    
    def pop(self):
        temp = self.peek()
        self.top = self.top.next
        return temp

"""
    A class representing a Stack data structure.
    
    Attributes:
    - top: Node - The top of the stack.
    
    Methods:
    - is_empty(): bool - Checks if the stack is empty.
    - push(data): None - Pushes an element or a list of elements onto the stack.
    - peek(): Any - Returns the data of the element at the top of the stack.
    - pop(): Any - Removes and returns the element at the top of the stack.
"""