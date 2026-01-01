import pytest
from src.sorting_searching.selection_sort import selection_sort
from src.sorting_searching.bubble_sort import bubble_sort


@pytest.mark.parametrize("input_arr, expected", [
    ([5, 7, 8, 4,1], [1, 4, 5, 7, 8]), # Standard Unsorted
    ([1, 2,3], [1, 2, 3]),             # Sorted
    ([], []),                          # Empty list
    ([1], [1]),                        # Single Element
    ([5, 2, 5, 1], [1, 2, 5, 5])       # Duplicate Element
])
def test_selection_sort(input_arr, expected):
    selection_sort(input_arr)
    assert input_arr == expected


@pytest.mark.parametrize("input_arr, expected", [
    ([5, 7, 8, 4,1], [1, 4, 5, 7, 8]), # Standard Unsorted
    ([1, 2,3], [1, 2, 3]),             # Sorted
    ([], []),                          # Empty list
    ([1], [1]),                        # Single Element
    ([5, 2, 5, 1], [1, 2, 5, 5])       # Duplicate Element
])
def test_bubble_sort(input_arr, expected):
    bubble_sort(input_arr)
    assert input_arr == expected