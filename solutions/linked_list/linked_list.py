class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  
  
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
    
    def __str__(self):
        result = ""

        current_node = self.head
        while current_node != None:
            result += f"{{{current_node.data}}} -> "
            current_node = current_node.next
        result += "NULL"
    
    def includes(self, value):
        current_node = self.head
        while current_node != None:
            if current_node.data == value:
                return True
        return False
    
for element in [1, 2,3]:
    print(element," ")

