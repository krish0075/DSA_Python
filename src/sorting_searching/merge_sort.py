def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                k += 1
            else:
                arr[k] = right_arr[j]
                j += 1
                k += 1

        if i < len(left_arr):
            while i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1
                k += 1
        if j < len(right_arr):
            while j < len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1


def merge_sort_reverse(input_arr):
    if len(input_arr) > 1:
        mid = len(input_arr) // 2
        left_arr = input_arr[:mid]
        right_arr = input_arr[mid:]
        merge_sort_reverse(left_arr)
        merge_sort_reverse(right_arr)
        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] >= right_arr[j]:
                input_arr[k] = left_arr[i]
                i += 1
                k += 1
            else:
                input_arr[k] = right_arr[j]
                j += 1
                k += 1

        if i < len(left_arr):
            while i < len(left_arr):
                input_arr[k] = left_arr[i]
                i += 1
                k += 1
        if j < len(right_arr):
            while j < len(right_arr):
                input_arr[k] = right_arr[j]
                j += 1
                k += 1