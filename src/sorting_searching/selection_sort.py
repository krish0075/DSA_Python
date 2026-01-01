def selection_sort(arr):
    """
    Sorts a list of numbers using a Selection Sort algorithm.

    INTUITION:
    Maintain two subsets: sorted and unsorted. In every iteration, find the minimum element from the unsorted subset and
    'select' it to move to the end of sorted subset.

    Time Complexity: O(N^2) - Two nested loops.
    Space Complexity: O(1) - In-place sorting.
    """
    n = len(arr)
    for i in range(n):
        # Assume the current position is the minimum
        min_index = i

        # Scan the rest of the list to find the actual minimum
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]