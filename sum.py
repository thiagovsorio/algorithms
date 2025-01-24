
def sum_divide_and_conquer(arr):

    if len(arr) <= 1:
        return arr[0] if arr else 0

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_sum = sum_divide_and_conquer(left_half)
    right_sum = sum_divide_and_conquer(right_half)
    
    return left_sum + right_sum

def main():
    arr = [1,2,3,773]

    total = 0
    total = sum_divide_and_conquer(arr)
    print(total)
main()