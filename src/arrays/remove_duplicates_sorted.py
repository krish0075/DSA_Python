"""
Problem: How to remove duplicates form a sorted array
Patter: Two pointers (slow & fast)
Time complexity: O(n)
Space complexity: O(1) - In-place
"""
def remove_duplicates_sorted(arr):
    if not arr:
        return 0
    n = len(arr)
    i = 0
    j = i + 1
    while j < n:
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
        j += 1

    return i # Number of unique elements