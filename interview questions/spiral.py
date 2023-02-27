"""
How would you write a program to move inside a square spiral? Start at the upper left corner of the square and walk its edges clockwise.
Just before re-approaching the upper left corner, spiral into the square instead, ultimately arriving at the center of the square.

                                                X X X X X X X X X
                                                                X
                                                X X X X X X X   X
                                                X           X   X
                                                X   X X X   X   X
                                                X   X       X   X
                                                X   X X X X X   X
                                                X               X
                                                X X X X X X X X X


create directional indicators using tuples:
right (1, 0)
down (0, 1)
left (-1, 0)
up (0, -1)

while length isn't reached increment the location with the current direction
example:
starting at (0, 1) we're adding right(1, 0) until reaching (7, 1)
then decrement the length by 1
switch to the next direction i.e down(0, 1) and continue until reaching (7, 7) etc
decrement length until it's 1

upper left corner is (0, 0) so the start location is (0, 1)

"""
from itertools import cycle

left = (1, 0)
down = (0, 1)
right = (-1, 0)
up = (0, -1)

dir = cycle([left, down, right, up])

length = 8

location = (0, 1)

print(f'starting at {location}')
while length:
    curr_dir = next(dir)
    for i in range(length - 1):
        location = tuple(map(sum, zip(location, curr_dir)))
        print(location)
    length -= 1




