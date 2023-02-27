from itertools import dropwhile
from operator import eq


def twoSum(nums, target: int):
    d = dict((enumerate(nums)))
    nums.sort()
    nums2 = nums[::-1]
    for num1 in nums:
        for num2 in nums2:
            if num2 + num1 > target:
                continue
            if num1 + num2 == target:
                return [list(d.values()).index(num1), list(d.values()).index(num2)]


q1 = ([2, 7, 11, 15], 9)
q2 = ([3, 2, 4], 6)
print(twoSum(*q1))
