"""
Problem: Find an element in an array using Linear Search
Pattern: Traversal
Time Complexity: O(n)
Space Complexity: O(1)
"""


def linear_search(arr, x):
    n = len(arr)

    for i in range(n):
        if arr[i] == x:
            return i
    return -1