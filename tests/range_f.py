import operator


def my_range(start=0, stop=None, step=1):

    if not stop:
        stop = start
        start = 0

    if start < stop:
        op = operator.le
        stop -= 1
    else:
        op = operator.ge
        stop += 1

    while op(start, stop):
        yield start
        start += step


print(list(my_range(10)))
print(list(range(10)))

print(list(my_range(1, 10, 2)))
print(list(range(1, 10, 2)))

print(list(my_range(0, -10, -2)))
print(list(range(0, -10, -2)))
