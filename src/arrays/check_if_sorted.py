"""
Problem: Check if an array is sorted
Pattern:
Time Complexity: O(n)
Space Complexity: O(1)
"""
def check_if_sorted(arr):
    n = len(arr)

    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False

    return True