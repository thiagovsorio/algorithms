def selection_sort(arr):
    sorted_arr = []
    
    for i in range(len(arr)):
        smallest = findSmallestElement(arr)
        sorted_arr.append(arr.pop(smallest))

    return sorted_arr


def findSmallestElement(arr):
    smallest = arr[0] 
    smallest_index = 0 
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

print(selection_sort([1,2,3]))
