"""
[18,67,2,54], 20 -> True
[12,3,5,7] , 4 -> False

O(n^2)

assuming the list is small and constant i.e 5

one long if (i[0] + i[1] == n...

if running through the list each time

list(sum([1,2,3,5])

list(map(sum, [18,67,2,54]))[0] == n
"""
from my_timeit.main import timeit

class MyCompare:

    def parse_list(self, l: list):
        """constant size"""
        self.l = l.sort()
        map(lambda a, b: self.sums.update({a + b, a + b}), self.l)
        self.sums.update({i + j: i + j} for i in self.l for j in self.l)

    def is_sum_exist(self, n):
        return self.sums.get(n, False)


def find_if_equal(l: list, n: int) -> bool:
    for i in l:
        for j in l:
            if i == j:
                continue
            if i + j == n:
                return True
    return False


def find_if_equal2(l: list, n: int) -> bool:
    for i in l:
        return any(map(lambda j: j + i == n and not i == j, l))


def find_if_equal3(l: list, n: int) -> bool:
    l.sort()
    for i in l:
        if l[0] !=i and l[0] + i > n:
            break
        return any(map(lambda j: j + i == n and not i == j, l))


print(find_if_equal2([18, 67, 2, 54], 20), timeit(find_if_equal2, ([18, 67, 2, 54], 20)))
print(find_if_equal2([12, 3, 5, 7], 6), timeit(find_if_equal2, ([12, 3, 5, 7], 6)))
print(find_if_equal2([12, 3, 5, 7], 6), timeit(find_if_equal2, ([12, 3, 5, 7], 6)))
