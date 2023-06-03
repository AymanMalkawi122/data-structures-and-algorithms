from ..stack_and_queue.stack import Stack


class QueuePseudo:
    def __init__(self):
        """
        Initializes a new instance of the QueuePseudo class.
        Creates a main stack and a backup stack.
        """
        self.main_stack = Stack()
        self.backup = Stack()

    def __dump_backup(self):
        while not self.backup.is_empty():
            self.main_stack.push(self.backup.pop())

    """
        Moves all elements from the backup stack to the main stack.
    """

    def is_empty(self):
        return self.backup.is_empty() and self.main_stack.is_empty()

    """
        Checks if the queue is empty.
        Returns True if both main_stack and backup are empty, False otherwise.
    """

    def enqueue(self, data):
        self.backup.push(data)
        if self.main_stack.is_empty():
            self.__dump_backup()

    """
        Adds an element to the back of the queue.
        If the main_stack is empty, moves elements from the backup stack to the main stack.
    """

    def peek(self):
        return self.main_stack.peek()

    """
        Retrieves the element at the front of the queue without removing it.
        Returns the top element of the main_stack.
    """

    def dequeue(self):
        if self.main_stack.is_empty():
            self.__dump_backup()
        return self.main_stack.pop()

    """
    Removes and returns the element at the front of the queue.
    If the main_stack is empty, moves elements from the backup stack to the main stack.
    """
