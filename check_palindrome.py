
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


if __name__ == '__main__':
    print(check_palindrome(123454321))