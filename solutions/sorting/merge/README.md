# merge Sort

* Merge sort is a divide-and-conquer algorithm that works by dividing the input array into smaller halves, sorting them individually, and then merging them back together to create a sorted array.
* It starts by dividing the array into two halves recursively until each subarray contains only one element or is empty. Then, it merges the subarrays by comparing the elements and placing them in the correct order.
* This process continues until the entire array is sorted. Merge sort has a time complexity of O(n log n), which makes it efficient for sorting large arrays.
* By breaking down the sorting process into smaller and manageable parts, merge sort provides a reliable and efficient method for sorting arrays.

## Pseudocode

```python ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

## Trace

**Sample Array: [3, 1, 4, 2]**

![image](./assets/Screenshot%202023-07-12%20174528.png)

### step 1

split current array becuse it is too big

### step 2

split current array becuse it is too big

### step 3

merge requires arrays to be sorted and an array with a single element is always sorted, so mergeing a two single element arrays into one array requires one comparision step

### step 4 - 6

when merging multi element sorted arrays we start by the smallest element and to find it we start with the first index for both arrays and compare them to get the smallest value then we incremint the index that had the smallest element untill we reach the end of one or both arrays

## Efficency

***Time***: O(n log(n))

the merge or split opiration takes around n steps for each level and the number of levels required to reach single element arrays is always log(n)

***Space***: O(n)

 the algorithm recursively divides the array into smaller subarrays, additional memory is required to store the temporary arrays for each level of recursion.
