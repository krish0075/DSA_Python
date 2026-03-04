"""
Problem: Find the second distinct largest element in an unsorted array
Pattern: Single Pass / Tracking values
Time complexity: O(n)
Space complexity: O(1)
"""

def find_second_largest(arr):
    n = len(arr)
    if n < 2:
        raise ValueError("Array should contain at least 2 elements.")
    largest = float("-inf")
    s_largest = float("-inf")

    for i in range(n):
        if arr[i] > largest:
            s_largest = largest
            largest = arr[i]

        elif arr[i] > s_largest and arr[i] != largest:
            s_largest = arr[i]

    return s_largest