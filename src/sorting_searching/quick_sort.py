def quick_sort(arr, low, high):
    """
    Sorts a list using the Quick Sort algorithm (Divide and Conquer).

    INTUITION:
    Pick a 'pivot' element. Rearrange the array so that everything smaller
    than the pivot is on the left, and everything larger is on the right.
    Then, recursively repeat this for the left and right halves.

    THE TRICK:
    The core of the algorithm is the 'Partition' step. Once an element is
    partitioned, it never moves again—it is in its perfect sorted spot.

    TIME COMPLEXITY:
    - Average/Best: O(n log n)
    - Worst: O(n^2) (When the pivot is always the smallest or largest element)

    SPACE COMPLEXITY: O(log n) - Due to the recursive call stack.

    Args:
        arr (list): The list to sort.
        low (int): Starting index.
        high (int): Ending index.
    """
    if low < high:
        # pi is the partitioning index; arr[pi] is now at the right place
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    """
    This function takes the last element as pivot, places the pivot element
    at its correct position in sorted array, and places all smaller elements
    to the left of pivot and all greater elements to the right.
    """
    pivot = arr[high]  # Choosing the last element as pivot
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element with the element at i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1