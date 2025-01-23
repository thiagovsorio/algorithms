def recursiveBinarySearch(arr: list[int], target: int) -> int:
    if len(arr) == 0:
        return -1
    left: int = 0
    right: int = len(arr) - 1
    mid: int = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
    if left > right:
        return -1
    return recursiveBinarySearch(arr[left:right], target)