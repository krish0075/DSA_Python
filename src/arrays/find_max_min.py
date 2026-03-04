"""
Problem: Find the maximum (or minimum) element in an unsorted array.
Pattern: Basic Array Traversal
Time Complexity: O(n)
Space Complexity: O(1)
"""

def find_max(arr):
    if not arr:
        raise ValueError("Input array is empty")
    n = len(arr)
    largest = smallest = arr[0]

    for i in range(1, n):
        largest = max(arr[i], largest)
        smallest = min(arr[i], smallest)

    return smallest, largest