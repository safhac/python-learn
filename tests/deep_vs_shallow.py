import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

deep = False

if deep:

    new_list = copy.copy(old_list)
    old_list[1][1] = 'AA'  # type: ignore

else:
    old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    new_list = copy.deepcopy(old_list)

print("Old list:", old_list)
print("New list:", new_list)