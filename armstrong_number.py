def check_armstrong_number(n):
    """
        Armstrong number is a number equal to sum of digits each raised to the power of number of digits.
    """
    num = n
    total = 0
    length = len(str(num))

    while num > 0:
        digit = num % 10
        total = total + digit ** length
        num = num // 10
    return n == total


if __name__ == '__main__':
    print(check_armstrong_number(0))
    print(check_armstrong_number(153))
    print(check_armstrong_number(154))