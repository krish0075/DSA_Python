def check_armstrong_number(n):
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