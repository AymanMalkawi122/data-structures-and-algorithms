# array-insert-shift

we have an  array and we want to add an element to its center

## Whiteboard Process

![image](./assets/Screenshot%202023-05-04%20134937.png)

## Approach & Efficiency

I appended the new element to the end of the array then I kept shifting it with the element that came before it until the number of shifts reaches (array size / 2), at that point the new element will be shifted to the middle position.

### Time Complexity

 O(n) because we loop n/2 times and when our input is large the performance will be similar to looping n times

### Space Complexity

O(1) because regardless of the size of our input, the algorithm only allocates a constant number of variables  

## Solution

Just run the following code in any Python3 interpreter

```python
import math

def swap(arr, idx1, idx2):
    temp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = temp

def insert(arr, num):
    if len(arr)<2:
        arr.append(num)
        return arr

    size = len(arr)
    arr.append(num)
    
    i = size
    while i > math.ceil(size / 2):
        swap(arr, i, i-1)
        i -= 1
        
    return arr
    
print(insert([15, 25, 33, 42], 55))
print(insert([1, 2, 3], 5))

````
