# object Sort

Two sorting functions, object_sort and remove_leading_articles. The object_sort function performs a sorting operation on an array of objects, and it takes a compare_func argument to define the sorting criteria. The remove_leading_articles function is used as a helper function within the by_title comparator function to remove leading articles like "A," "An," or "The" from movie titles.

## Pseudocode

```python
Start with an array arr and its length n.

Loop from i = 0 to i = n - 1.

Within the outer loop, loop from j = 0 to j = n - i - 1.

Call the compare_func with arr[j] and arr[j + 1] as arguments to determine if the elements need to be swapped.

If the compare_func returns True, swap arr[j] and arr[j + 1].

Continue with the next iteration of the inner loop.

If no swaps occurred in an iteration of the outer loop, the array is already sorted, and the sorting process can be stopped.

```

## Efficency

***Time***: O(n^2)

The worst-case, average-case, and best-case time complexity of the bubble sort algorithm is O(n^2). This is because, in the worst case, the algorithm needs to compare and swap elements for every pair, leading to n*(n-1)/2 comparisons. In the best-case scenario, the array is already sorted, but the algorithm still needs to perform the n*(n-1)/2 comparisons.

***Space***: O(1)

 The space complexity of the bubble sort algorithm is O(1) because it sorts the elements in-place and does not require additional space proportional to the input size.
