import pytest
from src.sorting_searching.quick_sort import quick_sort


@pytest.mark.parametrize("input_arr, expected", [
    ([5, 7, 8, 4, 1], [1, 4, 5, 7, 8]), # Standard Unsorted
    ([1, 2, 3], [1, 2, 3]),             # Sorted
    ([], []),                           # Empty list
    ([1], [1]),                         # Single Element
    ([5, 2, 5, 1], [1, 2, 5, 5])        # Duplicate Element
])
def test_quick_sort(input_arr, expected):
    quick_sort(input_arr)
    assert input_arr == expected