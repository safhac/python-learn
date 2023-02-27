"""
Write a function to return the nth fibonacci number.
The first two can be assumed to be 1 and 1.
The third and fourth are then calculated to be 2 and 3.
"""
from time import time


def nth_fib(nth: int) -> int:
    fib = [1, 1]
    first, second = 0, 1
    while len(fib) < nth:
        fib.extend([fib[first] + fib[second]])
        first += 1
        second += 1
    print(fib[nth - 1])


def comp_nth_fib(nth: int) -> int:
    fib = [1, 1]
    fib += [(fib := [fib[1], fib[0] + fib[1]]) and fib[1] for _ in range(nth)]
    print(fib[nth - 1])

def un(nth):
    fib = [1, 1]
    for _ in range(nth):
        # print('(fib := [fib[1], fib[0] + fib[1]])')
        # print((fib := [fib[1], fib[0] + fib[1]]))
        print('(fib := [fib[1], fib[0] + fib[1]]) and fib[1]')
        # print((fib := [fib[1], fib[0] + fib[1]]) and fib[1])
        fib += [(fib := [fib[1], fib[0] + fib[1]]) and fib[1]]
        print(fib)
    # return fib[nth - 1]


timeit = lambda f, param: (start := time(), f(param), time() - start)[2]

# print(timeit(comp_nth_fib, 1000))
# print(timeit(nth_fib, 1000))
un(10)
"""
assuming the 1st numbers are 1 and 1
the function should return 2 if called with 1
at each iteration 
    sum num1 and num2 into a temporary variable "sum"
    save num2 into num1 and sum into num2

the nth sum
 
"""
