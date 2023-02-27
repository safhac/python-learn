class Solution:
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman_subs = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

    def romanToInt(self, s: str) -> int:
        accum = 0
        for sub in self.roman_subs:
            if sub in s:
                accum += self.roman_subs[sub]
                s = s.replace(sub, "", 1)
        for rom in list(s):
            accum += self.romans.get(rom, None)
        return accum


sol = Solution()
print(sol.romanToInt("III"))
# I, V, X,   L,  C,  D,   M
# 1, 5, 10, 50, 100, 500, 1000
# IV, IX
# XL, XC
# CD, CM
