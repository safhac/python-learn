"""

1. add the indexes to stacks open / closed
2. when a close is detected find it's pair in open

"""
from random import sample

string = "".join(sample(["(", ")"], counts=[5, 7], k=12))

opened = []
closed = []

print(f"{string=}")
def is_parense(s):

    while any(pair in s for pair in ['()', ')(']):

        s = s.replace('()', '').replace(')(', '')
        print(f"after change {s=}")
    return not s

print(is_parense(string))


