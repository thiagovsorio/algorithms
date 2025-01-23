# def quicksortReadable(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]

#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]

#         return quicksortOld(less) + [pivot] + quicksortOld(greater)

def quicksort(array):
    if len(array) < 2:
        return array

    pivot = array[0]

    less = []
    greater = []

    for item in array[1:]:
        if item <= pivot:
            less.append(item)
        else:
            greater.append(item)

    return quicksort(less) + [pivot] + quicksort(greater)


# print(quicksortReadable[5, 2, 3, 1, 4]))
print(quicksort([5, 2, 3, 1, 1, 4]))

