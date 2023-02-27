def sum_only_once(lst: list) -> int:
    return sum(i for i in lst if not lst.count(i) > 1)


list1 = [1, 1, 2, 3, 5, 5, 5]
list2 = [1, 2, 2, 3, 15, 5, 5]
list3 = [1, 1, 2, 23, 5, 45, 5]
