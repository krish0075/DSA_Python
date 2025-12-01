def count_digits(num: int):
    if num == 0:
        return 1
    input_num = abs(num)
    count = 0
    while input_num > 0:
        count += 1
        input_num = input_num // 10
    return count

if __name__ == '__main__':
    print(count_digits(15327689))