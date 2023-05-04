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
