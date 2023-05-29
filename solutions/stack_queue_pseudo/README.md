# stack queue pseudo

## Task: implement queue using stack data structure

## 1. Whiteboard Process

![image](./assets/whiteboard.png)

## 2. Approach & Efficiency

### Approach

* The ```QueuePseudo``` class maintains two stacks,```main_stack``` and ```backup```, to simulate a queue.

* Elements are ```enqueued``` by pushing them onto the backup stack.

* When an element needs to be ```dequeued``` or ```peeked```, the elements are moved from backup to main_stack (if necessary) using the ```__dump_backup``` method.

* ```Dequeuing``` an element is done by popping it from the main_stack.

* The ```is_empty``` method checks if both main_stack and backup are empty to determine if the queue is empty.

### Efficiency

* ```Enqueuing``` an element is a constant time operation since it involves only pushing onto the backup stack.

* ```Dequeuing``` an element and peeking at the front element may involve moving elements from backup to main_stack in the worst case, resulting in a time complexity of O(n), where n is the number of elements in the queue.

* The ```is_empty``` method has a constant time complexity since it only checks the top of the stacks.

## 3. Solution

* Overall, the enqueue operation is efficient with a constant time complexity. However, dequeuing and peeking operations may have a time complexity of O(n) in the worst case, where n is the number of elements in the queue.
