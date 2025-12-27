def reverse_array(nums, left, right):
    if left >= right:
        return None
    nums[left], nums[right] = nums[right], nums[left]
    reverse_array(nums, left + 1, right - 1)
    return None

def reverse_array_while(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

if __name__ == "__main__":
    arr = [10, 2, 3, 4, 5, 6, 7]
    reverse_array_while(arr)
    print(arr)
