""""
Problem: Move zeroes to the end
Pattern:
Time complexity: O(n)
Space complexity: O(1)
"""


def move_zeroes(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return
    i = 0
    while i < n:
        if arr[i] == 0:
            break
        i += 1
    if i == n:
        return
    j = i+1
    while j < n:
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1


if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 0,  5, 6, 7, 8, 9]
    move_zeroes(arr)
    print(arr)