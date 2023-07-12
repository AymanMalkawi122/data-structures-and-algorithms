def split(arr):
    return (arr[ : int(len(arr) / 2)], arr[int(len(arr) / 2) : ])

def merge(arr1, arr2):
    final_arr = []
    index1 = 0
    index2 = 0

    while index1 < len(arr1) and index2 < len(arr2):
        if arr1[index1] <    arr2[index2]:
            final_arr.append(arr1[index1])
            index1 += 1
        else:
            final_arr.append(arr2[index2])
            index2 += 1

    
    final_arr += arr1[index1:]
    final_arr += arr2[index2:]

    return final_arr

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    arr_split = split(arr)
    first_half = arr_split[0]
    second_half = arr_split[1]
    # print(arr_split)
    sorted_first_half = merge_sort(first_half)
    sorted_second_half = merge_sort(second_half)

    return merge(sorted_first_half, sorted_second_half)

print(merge_sort([1,2,3,4,5]))