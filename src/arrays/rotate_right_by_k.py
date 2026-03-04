"""
Problem: Rotate array right by k time.
Pattern: Reversal Technique
Time complexity: O(n)
Space: O(1)
"""
def reverse_array(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def rotate_right_by_k(arr, k):
    if not arr:
        return 
    n = len(arr)
    k = k % n
    reverse_array(arr, n-k, n-1)
    reverse_array(arr, 0, n-k-1)
    reverse_array(arr, 0, n-1)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    k = 3
    rotate_right_by_k(nums, k)
    print(nums)