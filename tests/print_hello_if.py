is_div_by = lambda num, by: not num % by

def print_hello(num, by):
    print("hello") if is_div_by(num, by) and by in [3, 15] else None


print_hello(15, 5)