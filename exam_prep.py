def find_second_largest_easy(arr):
    if len(arr) < 2:
        return -1
    arr_set = list(set(arr))
    arr_set.sort(reverse=True) # This operation has O(n log n) Time complexity
    return arr_set[1]

def find_second_largest(arr):
    if len(arr) < 2:
        return None
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num > first:
            second = num
    return second


if __name__ == '__main__':
    print(find_second_largest([1, 2, 3, 4, 5, 6, 7]))
    print(find_second_largest([1, 1]))