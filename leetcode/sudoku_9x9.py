import copy
from bisect import bisect
from typing import List
from itertools import islice

# globals
INDEXES = set(i for i in range(9))
NUMBERS = set(i for i in range(1, 10))

VERTICAL = ["top", "mid", "bot"]
HORIZONTAL = ["Left", "Center", "Right"]
INDEX_POINTS = [3, 6]

sudoku = [[None for _ in range(9)] for _ in range(9)]
empty_cells: dict = {}
HISTORY: dict = {}
UNUSED: dict = {}


def get_grid(row, col):
    get_vector = lambda vec, i: vec[bisect(INDEX_POINTS, i)]
    return get_vector(VERTICAL, row) + get_vector(HORIZONTAL, col)


def get_grid_nums(grid):
    grid_map = {
        "topLeft": [r[:3] for r in sudoku[:3]],
        "topCenter": [r[3:6] for r in sudoku[:3]],
        "topRight": [r[6:] for r in sudoku[:3]],
        "midLeft": [r[:3] for r in sudoku[3:6]],
        "midCenter": [r[3:6] for r in sudoku[3:6]],
        "midRight": [r[6:] for r in sudoku[3:6]],
        "botLeft": [r[:3] for r in sudoku[6:]],
        "botCenter": [r[3:6] for r in sudoku[6:]],
        "botRight": [r[6:] for r in sudoku[6:]],
    }
    return [num for row in grid_map[grid] for num in row if num]


def get_row(row):
    return [num for num in sudoku[row] if num]


def get_col(col):
    return [row[col] for row in sudoku if row[col]]


def test_cell(cell):
    grids = set(get_grid_nums(cell.grid))
    rows = set(get_row(cell.row))
    cols = set(get_col(cell.col))
    print(f"{cell} {rows=} {cols=} {grids=}")
    raise


def testing():
    print("testing")
    for row in range(9):
        for col in range(9):
            cell = EmptyCell(row, col)

            grids = set(get_grid_nums(cell.grid))
            rows = set(get_row(cell.row))
            cols = set(get_col(cell.col))
            if not len(grids) == 9:
                print(f"{cell} error in grid [{grids}]")
            if not len(rows) == 9:
                print(f"{cell} error in row {rows=}")
            if not len(cols) == 9:
                print(f"{cell} error cols {cols=}")


# solution 3
class EmptyCell:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.grid = get_grid(row, col)
        self.possibilities: dict = {}

    def __len__(self):
        return len(list(self.possibilities))

    def __repr__(self):
        return f"cell[{self.row}][{self.col}] {self.possibilities}"

    def update_possibilities(self):
        existing = set()
        grid = get_grid_nums(self.grid)
        row = get_row(self.row)
        col = get_col(self.col)
        for num in [grid + row + col]:
            existing.update(num)

        self.possibilities = NUMBERS - existing
        # if not len(self.possibilities):
        #     breakpoint()


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        global sudoku, empty_cells, HISTORY
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    empty_cells.update({(row, col): EmptyCell(row, col)})
                else:
                    sudoku[row][col] = int(board[row][col])  # type: ignore

        count = 0
        while len(empty_cells):
            for key, cell in empty_cells.items():
                cell.update_possibilities()
                empty_cells.update({key: cell})

            smallest = min(empty_cells.values(), key=len)
            # print(f'{len(empty_cells)=} {count=} {smallest=}')

            if not len(smallest.possibilities):
                # there must be a mistake
                # remove placements find unused possibilities and replace the number
                alternate = list(UNUSED.keys())[0]
                print(f"{alternate=} {len(HISTORY)=}")
                # restore the first junction
                print("pre restore")
                for r in sudoku:
                    print(r)
                sudoku, empty_cells, HISTORY, count = UNUSED.pop(alternate)
                print("post restore")
                for r in sudoku:
                    print(r)
                print(f"going back to {count} {len(empty_cells)=}")
                smallest, poss = alternate
                print(f"now with {poss} for {smallest}")
                empty_cells.update({(smallest.row, smallest.col): smallest})
                sudoku[smallest.row][smallest.col] = poss
                HISTORY.update({count: (smallest.row, smallest.col, poss)})

            else:
                poss = smallest.possibilities.pop()

                if len(smallest.possibilities):
                    print(f"{len(HISTORY)=} {count=}")
                    print("board pre save")
                    for r in sudoku:
                        print(r)
                    UNUSED.update(
                        {
                            (smallest, poss): (
                                copy.deepcopy(sudoku),
                                copy.deepcopy(empty_cells),
                                copy.deepcopy(HISTORY),
                                count,
                            )
                            for poss in smallest.possibilities
                        }
                    )
                    print(f"used {poss} for {smallest}")
                    print(
                        f"saving alternative {smallest.possibilities} {len(empty_cells)=}"
                    )
                else:
                    print(
                        f"single possibility for {smallest} {poss} {len(empty_cells)=} {count=}"
                    )

                sudoku[smallest.row][smallest.col] = poss
                HISTORY.update({count: (smallest.row, smallest.col, poss)})

            empty_cells.pop((smallest.row, smallest.col))
            count += 1

        print("solved")
        for r in sudoku:
            print(r)
        # for r in range(9):
        # for c in range(9):
        #     board[r][c] = str(sudoku[r][c])
        # testing()

        # print(str(sudoku[row][col]))
        # board[row][col] = chr(sudoku[row][col])


board1 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
board2 = [
    [".", ".", "9", "7", "4", "8", ".", ".", "."],
    ["7", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "2", ".", "1", ".", "9", ".", ".", "."],
    [".", ".", "7", ".", ".", ".", "2", "4", "."],
    [".", "6", "4", ".", "1", ".", "5", "9", "."],
    [".", "9", "8", ".", ".", ".", "3", ".", "."],
    [".", ".", ".", "8", ".", "3", ".", "2", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "6"],
    [".", ".", ".", "2", "7", "5", "9", ".", "."],
]
board3 = [
    [".", ".", "9", "7", "4", "8", ".", ".", "."],
    ["7", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "2", ".", "1", ".", "9", ".", ".", "."],
    [".", ".", "7", ".", ".", ".", "2", "4", "."],
    [".", "6", "4", ".", "1", ".", "5", "9", "."],
    [".", "9", "8", ".", ".", ".", "3", ".", "."],
    [".", ".", ".", "8", ".", "3", ".", "2", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "6"],
    [".", ".", ".", "2", "7", "5", "9", ".", "."],
]

board4 = [
    [".", ".", "9", "7", "4", "8", ".", ".", "."],
    ["7", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "2", ".", "1", ".", "9", ".", ".", "."],
    [".", ".", "7", ".", ".", ".", "2", "4", "."],
    [".", "6", "4", ".", "1", ".", "5", "9", "."],
    [".", "9", "8", ".", ".", ".", "3", ".", "."],
    [".", ".", ".", "8", ".", "3", ".", "2", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "6"],
    [".", ".", ".", "2", "7", "5", "9", ".", "."],
]

"""

[["5","1","9","7","4","8","6","3","2"]
,["7","8","3","6","5","2","4","1","9"]
,["4","2","6","1","3","9","8","7","5"]
,["3","5","7","9","8","6","2","4","1"]
,["2","6","4","3","1","7","5","9","8"]
,["1","9","8","5","2","4","3","6","7"]
,["9","7","5","8","6","3","1","2","4"]
,["8","3","2","4","9","1","7","5","6"]
,["6","4","1","2","7","5","9","8","3"]]

"""
Solution().solveSudoku(board4)

"""
class Vector:
    # vector structure

    def __init__(self, index: int, numbers: list, rowCol: ROW | COL):

        self.index = index
        self.vector = dict({k: int(v) for k, v in enumerate(numbers) if not v == "."})
        self.rowCol = rowCol
        self._complete = False
        self.missing = NUMBERS - set(self.vector.values())
        self.indexes = (i, get_cell_grid(self.rowCol, self.index, i) for i in (INDEXES - set(self.vector.keys())))

    @property
    def complete(self):
        return self._complete

    def set_complete(self, state):
        self._complete = state

    def update_vector(self, cell, number):
        self.numbers.update({cell: number})
        if len(self) == 9:
            self.complete = True
            self.missing = self.indexes = []
        else:
            self.missing: list = [
                num for num in "123456789" if num not in self.numbers.values()
            ]
            indexes = [i for i in "012345678" if int(i) not in self.numbers.keys()]
            for old_key in [key for key in self.indexes.keys() if not key in indexes]:
                self.indexes.pop(old_key)

    def get_cell_grid(self, cell_index):
        # build the grid key using bisect for a specific cell

        get_vector = lambda vec, i: vec[bisect(index_points, i)]

        if self.rowCol == "row":
            ver = get_vector(horizontal, cell_index)
            hor = get_vector(vertical, self.index)
        else:
            hor = get_vector(vertical, cell_index)
            ver = get_vector(horizontal, self.index)

        return hor + ver

    def __repr__(self):
        return f"{self.rowCol}:{self.index} {self.numbers}"

    def __len__(self):
        return len(self.vector)


class Board:
    def __init__(self, board):
        self.board: list = []
        self.rows: dict = {}
        self.cols: dict = {}
        self.update_vectors(board)
        self.complete: bool = False
        self.set_current()
        self.board = board

    def get_grid_nums(self, grid):
        grids = {
            "topLeft": self.board[0][:3] + self.board[1][:3] + self.board[2][:3],
            "topCenter": self.board[0][3:6] + self.board[1][3:6] + self.board[2][3:6],
            "topRight": self.board[0][6:] + self.board[1][6:] + self.board[2][6:],
            "midLeft": self.board[3][:3] + self.board[4][:3] + self.board[5][:3],
            "midCenter": self.board[3][3:6] + self.board[4][3:6] + self.board[5][3:6],
            "midRight": self.board[3][6:] + self.board[4][6:] + self.board[5][6:],
            "botLeft": self.board[6][:3] + self.board[7][:3] + self.board[8][:3],
            "botCenter": self.board[6][3:6] + self.board[7][3:6] + self.board[8][3:6],
            "botRight": self.board[6][3:6] + self.board[7][3:6] + self.board[8][3:6],
        }
        return grids[grid]

    def update_vectors(self, board: list):

        self.rows.update(
            {index: Vector(index, row, "row") for index, row in enumerate(board)}
        )
        self.cols.update({i: Vector(i, [r[i] for r in board], "col") for i in range(9)})

    def set_current(self):
sets
the
vector
with the least possibilities
        rows = list(filter(lambda row: not row.complete, self.rows.values()))
        cols = list(filter(lambda col: not col.complete, self.cols.values()))
        # our Vectors override __len__
        self.current = max(rows + cols, key=len)
        # update perpendicular vectors
        if self.current.rowCol == "row":
            self.perps = [
                col
                for col in self.cols.values()
                if str(col.index) in self.current.indexes.keys()
            ]
        else:
            self.perps = [
                row
                for row in self.rows.values()
                if str(row.index) in self.current.indexes
            ]

    def insert_number(self, cell, num):
        # insert the number into the board, update the Board and Vector objects state
        if self.current.numbers.get(cell):
            breakpoint(self, cell, num)
            print('not emp')

        self.current.update_vector(cell, num)

        if "row" in self.current.rowCol:
            self.rows.update({self.current.index: self.current})
            print(f"before {self.board}")
            self.board[self.current.index][cell] = num
            print(f"after {self.board}")
        else:
            self.cols.update({self.current.index: self.current})
            print(f"before {self.board}")
            self.board[cell][self.current.index] = num
            print(f"after {self.board}")

        if self.current.complete:
            print(self.current, "complete")
            self.set_current()


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        sudoku = Board(board)
        curr = sudoku.current
        print(f"starting with {curr} missing {curr.missing}")
        while not sudoku.complete:

            if curr is not sudoku.current:
                curr = sudoku.current
                print(f"solving {curr} missing {curr.missing}")
            # possibilities = { number : [ available indexes ]
            possibilites: dict = {}

            # filter unavailable indexes
            for index, grid in sudoku.current.indexes.items():
                # get the grid and the perpendicular vector of the cell
                perp = list(filter(lambda p: p.index == int(index), sudoku.perps))[0]

                # update the possible placements of the missing numbers
                for num in sudoku.current.missing:

                    if not num in sudoku.get_grid_nums(grid) + [perp.numbers.values()]:
                        places = possibilites.get(num, [])
                        possibilites.update({num: places + [index]})

            # sort the numbers by possibilities
            print(f"{possibilites=}")
            if len(possibilites) == 1:
                print("")
            smallest, keys = min(zip(possibilites.keys(), possibilites.values()))
            if len(keys) == 1:
                print("single solution")

            sudoku.insert_number(int(keys[0]), smallest)



board2 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    ["1", "9", "8", ".", "4", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", "5", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
    ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
    ["3", ".", ".", ".", "8", ".", ".", "7", "9"],
]
Solution().solveSudoku(board1)

row1, row2, row3, row4, row5, row6, row7, row8, row9 = [RowCol(k, v) for k, v in enumerate(board)]
col1, col2, col3, col4, col5, col6, col7, col8, col9 = [RowCol(i, [row[i] for row in board]) for i in range(9)]

# rows = [row for row in board]
# cols = [[row[i] for row in board] for i in range(9)]
# topLeft = rows[0][:3] + rows[1][:3] + rows[2][:3]
# topCenter = rows[0][3:6] + rows[1][3:6] + rows[2][3:6]
# topRight = rows[0][6:] + rows[1][6:] + rows[2][6:]
# midLeft = rows[3][:3] + rows[4][:3] + rows[5][:3]
# midCenter = rows[3][3:6] + rows[4][3:6] + rows[5][3:6]
# midRight = rows[3][6:] + rows[4][6:] + rows[5][6:]
# botLeft = rows[6][:3] + rows[7][:3] + rows[8][:3]
# botCenter = rows[6][3:6] + rows[7][3:6] + rows[8][3:6]
# botRight = rows[6][3:6] + rows[7][3:6] + rows[8][3:6]


# col1, col2, col3, col4, col5, col6, col7, col8, col9 = cols
# row1, row2, row3, row4, row5, row6, row7, row8, row9 = rows
#

"""
"""
Left, Middle, Right

Top,
Center,
Bottom

my
1
st
idea is to
create
a
Row / Col
structure
that
holds
the
col / row
index
the
provided
input
a
list
of
all
the
possible
solutions


class RowCol:
    row: bool
    col: bool
    index: int
    input: list
    solved: bool
    solution: list
    possible_solutions: list
    of
    lists


the
idea is to
get
a
starting
point(row or col)
with the least number of possibilities
looping
over
the
1
st
possible
solution
checking
the
possibilities
of
the
overlapping
cells
of
the
perpendicular
element.
if all the overlapping cell values fit the possibilities of the perpendicular row or column
if the overlapping cells don't fit the perpendicular element remove it from the possibilities list and check the next one.
since
there
can
only
be
one
solution
the
number
of
possibilities
of
none
solved
row / cols
should
lessen
with each iteration
making
the
loop
run
faster
each
time

I
will
create
a
function
that
maps
all
the
possibilities
according
to
the
input
for the element.
    for example:

dry
run:
[["5", "3", ".", ".", "7", ".", ".", ".", "."],
 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
 [".", "9", "8", ".", ".", ".", ".", "6", "."],
 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
 [".", "6", ".", ".", ".", ".", "2", "8", "."],
 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

solution
2
----------
create
a
dict
with the keys being the input and the value representing the index of the value
for example:
    row
0
clue is
["5", "3", ".", ".", "7", ".", ".", ".", "."]
input = {
    "5": 0,
    "3": 1,
    "7": 4
}
so
the
keys
can
only
be
1, 2, 4, 5, 6, 8 and 9
and their
value
can
be
2, 3, 5, 6, 7 and 8

as I
run
through
the
1
st
iteration
I
realise
the
solution
must
be
recursive

a.list
the
missing
numbers
b.filter
possible
placements
on
vectors and grids
i.e
how
many
vectors
the
number
can
be
placed
c. if we
find
a
single
solution
it
must
be
used
d.update
the
missing
numbers and possibilities, this
should
create
another
single
solution
c.list
the
possible
numbers in the
perpendicular
vectors
c.list
the
possible
numbers in 3
x3
grids
where
the
indexes
reside

for example
    col1 = ["5", "6", ".", "8", "4", "7", ".", ".", "."]
missing
1, 2, 3, 9
indexes
3, 7, 8, 9
we
need
to
check
rows
3, 7, 8 and 9
then
check
the
top and bottom
left
grids
row3
has
6, 8, 9
row7
has
2, 6, 8
row8
has
1, 4, 5, 9
row9
has
7, 8, 9
so
the
only
row
we
can
place
9 is row7
this
case
saves
the
checking
of
the
3
x3
grid
since
there
's only 1 solution

col1 = ["5", "6", ".", "8", "4", "7", "9", ".", "."]
missing
1, 2, 3
indexes
3, 8, 9
index
3 is in the
top - left
grid
indexes
8 and 9
are in the
bottom
left
grid
top
left
grid
contains
3
bottom
left
only
contains
6
in row3
we
can
place
1, 2
in row7
we
can
place
1, 3
in row8
we
can
place
2, 3
in row9
we
can
place
1, 2, 3

col1 = ["5", "6", "1", "8", "4", "7", "9", ".", "."]
missing
2, 3
indexes
8, 9

col1 = ["5", "6", "1", "8", "4", "7", "9", "2", "3"]

our
sudoku
looks
like
this
[["5", "3", ".", ".", "7", ".", ".", ".", "."],
 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
 ["1", "9", "8", ".", ".", ".", ".", "6", "."],
 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
 ["9", "6", ".", ".", ".", ".", "2", "8", "."],
 ["2", ".", ".", "4", "1", "9", ".", ".", "5"],
 ["3", ".", ".", ".", "8", ".", ".", "7", "9"]]

row8 = ["2", ".", ".", "4", "1", "9", ".", ".", "5"]
has
the
most
numbers
missing
3, 6, 7, 8
indexes
2, 3, 7, 8

indexes
2, 3
are in the
left
bottom
grid
index
7, 8
are in the
bottom
right
grid
col2
has
3, 6, 9
col3
has
8
col7
has
2
col8
has
6, 7, 8
grid
left - bottom
has
6
grid
right - bottom
has
2, 5, 7, 8, 9

3
can
be
place in all
grids and all
cols except col2
6
can
be
placed in col7
since
it
's present in the bottom left grid and col8
one
solution
row8 = ["2", ".", ".", "4", "1", "9", "6", ".", "5"]
7 and 8
can
be
only
be
placed in cols
2 and 3
since
they
're present in right-bottom grid
col3
has
8
so
we
must
place
7 in col3 and 8 in col2
so
we
only
have
one
solution
for
    6, 7, 8 and thus
3
row8 = ["2", "8", "7", "4", "1", "9", "6", "3", "5"]

after
solving
row
8:
[["5", "3", ".", ".", "7", ".", ".", ".", "."],
 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
 ["1", "9", "8", ".", ".", ".", ".", "6", "."],
 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
 ["9", "6", ".", ".", ".", ".", "2", "8", "."],
 ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
 ["3", ".", ".", ".", "8", ".", ".", "7", "9"]]

col6
has
6
numbers
col6 = ["7", "9", ".", "6", ".", "2", ".", "1", "8"]
missing
3, 4, 5
indexes
3, 5, 7
grids
topCenter, middleCenter, bottomCenter
row3
missing
2, 3, 4, 5, 7
row5
missing
2, 5, 6, 7, 9
row7
missing
1, 3, 4, 5, 7
topCenter
has
1, 5, 7, 9
midCenter
has
2, 3, 6, 8
botCenter
has
1, 4, 8, 9

3
has
2
options
since
it
exists in midCenter
but
missing
from row3 and row7
4
has
1
option
since
it
exists in botCenter and row5
one
solution
col6 = ["7", "9", "4", "6", ".", "2", ".", "1", "8"]
missing
3, 5
indexes
5, 7
hence
3
has
one
solution and only
one
option
for
    col6 = ["7", "9", "4", "6", "5", "2", "3", "1", "8"]

after
solving
col1, row8, col6:
[["5", "3", ".", ".", "7", ".", ".", ".", "."],
 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
 ["1", "9", "8", ".", "4", ".", ".", "6", "."],
 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
 ["4", ".", ".", "8", "5", "3", ".", ".", "1"],
 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
 ["9", "6", ".", ".", "3", ".", "2", "8", "."],
 ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
 ["3", ".", ".", ".", "8", ".", ".", "7", "9"]]

row7 = ["9", "6", ".", ".", "3", ".", "2", "8", "."]
missing
1, 4, 5, 7
indexes
3, 4, 6, 9
grids
botLeft, botCenter, botRight

col3
has
7, 8
col4
has
1, 4, 8
col6
has
3, 5, 9
col9
has
1, 3, 6, 7, 8

botLeft
has
2, 3, 6, 7, 8, 9
botCenter
has
1, 3, 4, 8, 9
botRight
has
2, 3, 5, 6, 7, 8, 9

1
col3
one
solution
["9", "6", "1", ".", "3", ".", "2", "8", "."]
4
col9
one
solution
["9", "6", "1", ".", "3", ".", "2", "8", "4"]
5
col4
["9", "6", "1", "5", "3", ".", "2", "8", "4"]
7
col6
one
solution
["9", "6", "1", "5", "3", "7", "2", "8", "4"]

[["5", "3", ".", ".", "7", ".", ".", ".", "."],
 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
 ["1", "9", "8", ".", "4", ".", ".", "6", "."],
 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
 ["4", ".", ".", "8", "5", "3", ".", ".", "1"],
 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
 ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
 ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
 ["3", ".", ".", ".", "8", ".", ".", "7", "9"]]

"""
