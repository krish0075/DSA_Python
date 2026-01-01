def bubble_sort(arr):
    """
    Sorts a list of numbers using bubble sort algorithm

    INTUITION:
    Repeatedly step through the list, compare adjacent elements, and swap them if they are in the wrong order.
    With each full pass through the list, the largest element "bubbles up" to its correct position at the end of the list.

    THE TRICK:
    After the first pass, the largest element is guaranteed to be at the last index of the list.
    After the second pass, the smallest element is guaranteed to be at the second-to-last index.
    We can optimize by reducing the range of inner loop by 1 each time.

    Time Complexity:
    - Worst/Average: O(n^2)
    - Best: O(n) (If the list is already sorted, and we use a 'swapped' flag)

    Space Complexity: O(1) - In-place sorting

    Args:
        arr (list): A list of comparable elements to be sorted

    """
    n = len(arr)
    for i in range(n-2, -1, -1):
        swapped = False
        for j in range(0, i+1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break