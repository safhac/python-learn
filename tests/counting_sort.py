my_arr = [1, 4, 1, 2, 7, 5, 2]


def counting_sort(arr: list) -> list:
    count_index = [None] * 10
    print(count_index)
    for i in range(10):
        count_index[i] = arr.count(i)
        if i:
            count_index[i] += count_index[i - 1]

    print(count_index)
    count_index = [0] + count_index[:-1]
    print(count_index)


counting_sort(my_arr)
