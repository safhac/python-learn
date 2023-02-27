"""
You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.

5F3Z-2e-9-w", k = 4

1. split the string to a list
2. check the list for strings
3. the 1st cell must be min 1 and max k
4. the other cells must be k
5. convert the strings to upper
6. join with a "-" and return
"""
from itertools import islice


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = "-".join(s.replace("-", "")[i : i + k] for i in range(0, len(s), k))
        return res[0 : len(res) - 1]


print(Solution().licenseKeyFormatting("2-5g-3-J", 2))
