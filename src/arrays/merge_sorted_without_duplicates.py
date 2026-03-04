def merge_sorted_without_duplicates(arr1, arr2):
    n, m = len(arr1), len(arr2)
    i = j = 0
    merged_array = []
    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            if len(merged_array) == 0 or merged_array[-1] != arr1[i]:
                merged_array.append(arr1[i])
            i += 1
        else:
            if len(merged_array) == 0 or merged_array[-1] != arr2[j]:
                merged_array.append(arr2[j])
            j += 1
    while i < n:
        if len(merged_array) == 0 or merged_array[-1] != arr1[i]:
            merged_array.append(arr1[i])
            i += 1

    while j < m:
        if len(merged_array) == 0 or merged_array[-1] != arr2[j]:
            merged_array.append(arr2[j])
            j += 1
    return merged_array