numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]


class RomanNumerals:
    def to_roman(self, val):
        res = ""
        table = list(zip(integers, numerals))
        for cap, roman in table:
            d, m = divmod(val, cap)
            res += roman * d
            val = m
            if not any([d, m]):
                break

        return res

    def from_roman(self, roman_num):
        table = dict(zip(numerals, integers))
        index = 0
        sum = 0
        pair = ""
        size = len(roman_num)
        while index < size:
            if index < size - 1:
                pair = roman_num[index:index + 2]
            if pair in table:
                sum += table.get(pair)
                index = index + 2
                pair = ""
            else:
                sum += table.get(roman_num[index])
                index += 1

        return sum


rn = RomanNumerals()

num = 2291
print(f"{num=}")
roman = rn.to_roman(num)
print(f"{roman=}")
print(f"{rn.from_roman(roman)=}")
