def o_n2(arr):
    n = len(arr)
    max_sum = arr[0]
    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += arr[end]
            if current_sum > max_sum:
                max_sum = current_sum


def single_loop(arr):
    n = len(arr)
    max_sum = arr[0]
    current_sum = arr[0]
    for i in range(1, n):
        current_sum = max(current_sum + arr[i], arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


arr1 = [3, 4, -9, 1, 2]
arr2 = [1, 2, 3]
arr3 = [-1, -2, -3]

[print(single_loop(a)) for a in [arr1, arr2, arr3]]
