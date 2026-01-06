def insertion_sort(input_arr):
    n = len(input_arr)
    for i in range(1, n):
        j = i-1
        key = input_arr[i]
        while j >= 0 and input_arr[j] > key:
            input_arr[j+1] = input_arr[j]
            j -= 1
        input_arr[j+1] = key

def insertion_sort_reverse(input_arr):
    n = len(input_arr)
    for i in range(1, n):
        key = input_arr[i]
        j = i-1
        while j >= 0 and input_arr[j] < key:
            input_arr[j+1] = input_arr[j]
            j -= 1
        input_arr[j+1] = key
