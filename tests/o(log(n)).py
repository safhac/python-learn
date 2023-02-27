"""
Consider the following problem:

L is a sorted list containing n signed integers (n being big enough),
for example [-5, -2, -1, 0, 1, 2, 4] (here, n has a value of 7).
If L is known to contain the integer 0, how can you find the index of 0 ?
"""

L = [-5, -2, 0, -1, 1, 2, 4, -5, -2, -1, 1, 2, 4]
L.sort()
print(L)

def find_zero(b):
    a = 0
    while True:
        h = (a + b) // 2  ## // is the integer division, so h is an integer
        if L[h] == 0:
            return h
            break
        elif L[h] > 0:
            print('L[h] > 0')
            b = h
        elif L[h] < 0:
            print('L[h] < 0')
            a = h

print(find_zero(len(L) - 1))