def extract_digits(num: int):
    if num == 0:
        print(0)
    input_num = abs(num)
    while input_num > 0:
        last_digit = input_num % 10
        print(last_digit)
        input_num = input_num // 10


if __name__ == '__main__':
    print(extract_digits(-123))