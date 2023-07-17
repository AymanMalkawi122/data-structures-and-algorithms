def object_sort(arr, compare_func):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if cmp_func(arr[j], arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]


def by_year(obj1, obj2):
    return 

def by_title(obj1, obj2):