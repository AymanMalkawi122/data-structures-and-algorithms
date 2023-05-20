# stack and queue

## Task: implement a stack and queue data structure

## 1. Whiteboard Process

### not required

## 2. Approach & Efficiency

## Queue

### Time Complexity Analysis

* ```is_empty()``` function: This function has a time complexity of ```O(1)``` as it performs a simple comparison operation.

* ```__enqueue_single()``` function: This function has a time complexity of ```O(1)``` as it inserts a new element at the back of the queue.

* ```enqueue()``` function: The time complexity of this function depends on the length of the input data. If the input data is a list with ```n``` elements, the time complexity is ```O(n)``` as it iterates through each element and calls the ```__enqueue_single()``` function.

* ```peek()``` function: This function has a time complexity of ```O(1)``` as it simply returns the data of the element at the front of the queue.

* d```equeue()``` function: This function has a time complexity of ```O(1)``` as it removes the element at the front of the queue.
Space Complexity Analysis:

## Stack

### Time Complexity Analysis

* ```__push_single()``` function: This function has a time complexity of ```O(1)``` as it inserts a new element at the top of the stack.

* ```push()``` function: The time complexity of this function depends on the length of the input data. If the input data is a list with n elements, the time complexity is ```O(n)``` as it iterates through each element and calls the ```__push_single()``` function.

* ```peek()``` function: This function has a time complexity of ```O(1)``` as it simply returns the data of the element at the top of the stack.

* ```pop()``` function: This function has a time complexity of ```O(1)``` as it removes the element at the top of the stack.

## 3. Solution

* For the **Queue** class, it uses a linked list approach to represent a queue. It has methods to check if the queue is empty, enqueue elements at the back of the queue, peek at the element at the front of the queue without removing it, and dequeue the element at the front of the queue. It also has a private method to enqueue a single element.

* For the **Stack** class, it also uses a linked list approach to represent a stack. It has methods to check if the stack is empty, push elements onto the stack, peek at the element at the top of the stack without removing it, and pop the element at the top of the stack. It also has a private method to push a single element.
