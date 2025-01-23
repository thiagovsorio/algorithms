arr = [1,2,3,4,5,6,7,8,9,10]

def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        print(mid)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
def recursiveBinarySearch(arr, target, left, right):
    mid = (left + right) // 2
    if arr[mid] == target:
        print('found', mid)
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
    indexOfElement: int | None = recursiveBinarySearch(arr, target, left, right)
    return indexOfElement

target = 10
print('index of element', target, 'at given array is', recursiveBinarySearch(arr, 10, 0, len(arr) -1))
