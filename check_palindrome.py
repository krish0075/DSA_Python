
def check_palindrome(n):
    """
    Time Complexity: O(log10(N))
        The input is getting reduced by 10 everytime so time complexity is O(log10(N))
    Space Complexity: O(1)
        We are using 2 variables irrespective of the input number. so space complexity is Constant.
    """
    num = n
    result = 0
    while num > 0:
        last_digit = num % 10
        result = result * 10 + last_digit # Moves the existing number to 10th place and new number to unit place.
        num = num // 10
    return n == result

def check_palindrome_string(left, right, name):
    """
    This functions check if a string is palindrome or not.
        Time complexity: O(N) -- this will be N/2
        Space complexity: O(N)  -- Stack space actually it will be O(N/2)
    """
    if left >= right:
        return True
    if name[left] != name[right]:
        return False
    return check_palindrome_string(left+1, right-1, name)

def check_palindrome_string_while(name:str):
    """
    This function check if a string is palindrome or not using while loop
    Time Complexity: O(N) -- this will be N/2
    Spce complexity: O(1) -- this is constant
    """
    n = len(name)
    left = 0
    right = n-1
    while left < right:
        if name[left] != name[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == '__main__':
    # print(check_palindrome(123454321))
    name_str = 'momo'
    print(check_palindrome_string(0, len(name_str)-1, name_str))
    print(check_palindrome_string_while(name_str))