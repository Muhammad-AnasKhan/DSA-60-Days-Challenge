def find_numbers_in_range(arr, low, high, target_num):
    if low < 0:
        low = 0
    if high > len(arr) - 1:
        high = len(arr) - 1

    result = []

    for i in range(len(arr)):
        if arr[i] == target_num:
            result.append(target_num)

    return result


print(find_numbers_in_range([1,3,5,6,4,4,4,33,3333,3], 1, 20, 4))
