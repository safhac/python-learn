from functools import reduce
from typing import List


def get_sum(a, b):
    return a + b


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = nums[0]
        return [sum] + [sum := sum + i for i in nums[1:]]


nums1 = [1, 2, 3, 4]
nums2 = [1, 1, 1, 1, 1]
nums3 = [3, 1, 2, 10, 1]

print(Solution().runningSum(nums1))
print(Solution().runningSum(nums2))
print(Solution().runningSum(nums3))
