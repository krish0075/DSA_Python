"""
    Write a function to find the sum of numbers from 1 to N.
"""

def sum_numbers(sum, i, n):
    """
        This is an example of tail recursion. Recursive call is the last operation performed in the block.
        sum and i values are passed through recursive calls.
    """
    if i > n:
        print(sum) # base condition
        return None
    sum_numbers(sum + i, i + 1, n)

def sum_numbers_recursive(n):
    if n == 1:
        return 1
    return n + sum_numbers_recursive(n-1)

def factorial(n):
    """
        A function that returns the factorial of n using functional recursion.
    :param n:
    :return:
    """
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)


if __name__ == '__main__':
    print(factorial(5))