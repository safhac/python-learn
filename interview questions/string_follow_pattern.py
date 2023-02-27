"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.



Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false



Constraints:

    1 <= pattern.length <= 300
    pattern contains only lower-case English letters.
    1 <= s.length <= 3000
    s contains only lowercase English letters and spaces ' '.
    s does not contain any leading or trailing spaces.
    All the words in s are separated by a single space.


"""

from itertools import groupby


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        is_eq = lambda left, right: left == right
        get_left = lambda lst: lst[:mid + 1]
        get_right = lambda lst: lst[mid:]
        right_mirror = lambda lst: get_right(lst)[::-1]
        pat = [list(g) for _, g in groupby(pattern)]
        s_pat = [list(g) for _, g in groupby(s.split(" "))]
        if not len(pat) == len(s_pat):
            return False

        mid = len(pat) // 2
        """
        if both pattern and string left eq or not eq right return true else false:
        ie if both either anagrams or both are not anagrams  
        """
        print(f'{get_left(pat)=}')
        print(f'{right_mirror(pat)=}')
        print(f'{get_left(s_pat)=}')
        print(f'{right_mirror(s_pat)=}')
        pat_eq = is_eq(get_left(pat), right_mirror(pat))
        s_eq = is_eq(get_left(s_pat), right_mirror(s_pat))
        print(f'{pat_eq=}, {s_eq=}')
        if all([pat_eq, s_eq]) or not any([pat_eq, s_eq]):
            return True
        return False


print(Solution().wordPattern("abba", "dog cat cat dog")) # true
print(Solution().wordPattern("abba", "dog cat cat fish")) # false
print(Solution().wordPattern("abaaba", "dog cat fish fish cat dog")) # false
