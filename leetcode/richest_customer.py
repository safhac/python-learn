from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(list(map(sum, accounts)))


acc1 = [[1, 2, 3], [3, 2, 1]]
acc2 = [[1, 5], [7, 3], [3, 5]]
acc3 = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]

print(Solution().maximumWealth(acc1))
print(Solution().maximumWealth(acc2))
print(Solution().maximumWealth(acc3))
