from functools import reduce

# str1 = str(input('enter string 1'))
# str2 = str(input('enter string 2'))
# str3 = str(input('enter string 3'))
str1 = "hihowareyou"
str2 = "hiyourewelcome"
str3 = "higoodmorning"

first, second, third = '', '', ''


def logical():
        if str1 < str2:
                print("str1 < str2")
                if str1 < str3:
                        first = str1
                        print(f"str1 < str3 {first=}")
                        if str2 < str3:
                                second = str2
                                third = str3
                                print(f"str2 < str3 {second=} {third=}")
                        else:
                                second = str3
                                third = str2
                                print(f"str3 < str2 {second=} {third=}")
                else:
                        first = str3
                        second = str1
                        third = str2
                        print(f"str3 < str1 {first=} {second=} {third=}")


def anotherway():
        first = min({str1, str2, str3})
        third = max({str1, str2, str3})
        for s in {str1, str2, str3}:
                if not (s == first and s == third):
                        second = s
                        break
        print(f"{first=} {second=} {third=}")


anotherway()
