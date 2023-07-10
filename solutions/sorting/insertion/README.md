# Insertion Sort

The algorithm works by dividing the array into a sorted and an unsorted region. It iterates through the unsorted region and repeatedly selects an element (```current_value```), comparing it with elements in the sorted region, and shifting them to the right until finding the correct position for the key. Finally, it places the key at its sorted position.

## Pseudocode

```python Insert(int[] sorted, int value)
  initialize i to 0
  WHILE value > sorted[i]
    set i to i + 1
  WHILE i < sorted.length
    set temp to sorted[i]
    set sorted[i] to value
    set value to temp
    set i to i + 1
  append value to sorted

InsertionSort(int[] input)
  LET sorted = New Empty Array
  sorted[0] = input[0]
  FOR i from 1 up to input.length
    Insert(sorted, input[i])
  return sorted
```

## Trace

**Sample Array: [5, 2, 3, 4]**

![image](./assets/Screenshot%202023-07-10%20220606.png)

### step 1

we only have one element so it will always be grater than every element in the sorted section so it will be inserted into the first postion

### step 2

2 is less than 5 so it will be inserted into the first postion and 5 will be shifted to the right

### step 3

3 is less than 5 and gerater than the rest of the sorted section so it will be inserted into the second postion and 5 will be shifted to the right

### step 4

4 is less than 5 and gerater than the rest of the sorted section so it will be inserted into the third postion and 5 will be shifted to the right

## Efficency

***Time***: O(n^2)

The array is being traversed n times and each traversal takes n steps.

***Space***: O(1)

No additional space is being created. This array is being sorted in place…keeping the space at constant O(1).
