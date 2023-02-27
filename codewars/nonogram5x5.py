import numpy as np


possibilities5x5 = {
    (1,): [
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
    ],
    (2,): [[1, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 1, 1]],
    (3,): [[1, 1, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 1, 1]],
    (4,): [[1, 1, 1, 1, 0], [0, 1, 1, 1, 1]],
    (1, 1): [
        [1, 0, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 0, 1],
    ],
    (1, 1, 1): [[1, 0, 1, 0, 1]],
    (1, 2): [[1, 0, 1, 1, 0], [1, 0, 0, 1, 1], [0, 1, 0, 1, 1]],
    (2, 1): [[1, 1, 0, 1, 0], [1, 1, 0, 0, 1], [0, 1, 1, 0, 1]],
    (2, 2): [[1, 1, 0, 1, 1]],
    (3, 1): [[1, 1, 1, 0, 1]],
    (1, 3): [[1, 0, 1, 1, 1]],
}


class Clue:

    def __init__(self, clue, index, _type="ROW"):
        self.clue = clue
        self.index = index
        self._type = _type
        self.all_possibilities = possibilities5x5.get(self.clue, [])
        self.possibility_count = len(self.all_possibilities)
        self.filtered_possibilities = []
        self.solution = self.all_possibilities[0]
        self.solved = True if self.possibility_count == 1 else False

    def matching_possibilities(self, solved):
        return list(
            filter(
                lambda possibility: possibility[solved.index]
                                    == solved.solution[self.index],
                self.all_possibilities(),
            )
        )

    def __repr__(self):
        return f"{self._type} {self.index} {self.clue} {self.solution} {self.possibility_count}"


class Nonogram:


    def __init__(self, clues):

        self.clue_list: list[Clue] = []
        self.solution = np.zeros([5, 5], dtype=int)
        self.clues = clues

        # ragged nested sequences (non square) multi-dim array
        self.cols = np.array([possibilities5x5.get(clue) for clue in self.clues[0]], dtype=object)
        self.rows = np.array([possibilities5x5.get(clue) for clue in self.clues[1]], dtype=object)


    def as_tuple(self):
        return tuple((row.solution) for row in self.clue_list if row._type == "ROW")

    def unsolved_perpendiculars(self, _type):
        return list(
            filter(lambda clue: clue._type != _type and not clue.solved, self.clue_list)
        )

    def get_solved_indices(self):
        """
        create a dictionary with solved indices and values
        :return: a dictionary with the keys (col, row) and the single solution value
        """

        indices = dict()
        solved_items = list(filter(lambda clue: clue.solved, self.clue_list))

        for solved in solved_items:
            for i in range(5):
                key = self.col_row_tuple(solved, i)
                indices.update({key: solved.solution[i]})
        return indices

    def filter_possibilities(self, clue):
        """
        filter out clue possibilities that are incompatible with solved clues
        :param clue: the clue to filter
        :return: a list of filtered possibilities that match solved items
        """

        filtered = clue.all_possibilities
        # solved clues as dict
        as_dict = self.get_solved_indices()

        # matching indices of the clue and solved
        clue_indices = [self.col_row_tuple(clue, i) for i in range(5)]
        matching_indices = [key for key in clue_indices if key in as_dict.keys()]
        print(f"there are {len(matching_indices)=}")

        # for poss in clue.all_possibilities:

        print(f"{clue._type} {clue.index} has {len(filtered)} filtered possibilities")

        return filtered

    def solve(self):

        solutions = []

        return self.as_tuple()


# testing
import unittest

test1 = ((1, 1), (4,), (1, 1, 1), (3,), (1,)), ((1,), (2,), (3,), (2, 1), (4,))
test2 = ((1,), (3,), (1,), (3, 1), (3, 1)), ((3,), (2,), (2, 2), (1,), (1, 2))
test3 = ((3,), (2,), (1, 1), (2,), (4,)), ((2,), (3, 1), (1, 2), (3,), (1,))
sol1 = (
    (0, 0, 1, 0, 0),
    (1, 1, 0, 0, 0),
    (0, 1, 1, 1, 0),
    (1, 1, 0, 1, 0),
    (0, 1, 1, 1, 1),
)
sol2 = (
    (0, 0, 1, 1, 1),
    (0, 0, 0, 1, 1),
    (1, 1, 0, 1, 1),
    (0, 1, 0, 0, 0),
    (0, 1, 0, 1, 1),
)

sol3 = (
    (1, 1, 0, 0, 0),
    (1, 1, 1, 0, 1),
    (1, 0, 0, 1, 1),
    (0, 0, 1, 1, 1),
    (0, 0, 0, 0, 1),
)
tests = [test1, test2, test3]
sols = [sol1, sol2, sol3]

nono = Nonogram(test1)
print(nono.solve())
print(sol1)
# class NonogramTester(unittest.TestCase):
#
#     def test1(self):
#         nono = Nonogram(test1)
#         self.assertEqual(nono.solve(), sol1)


# def test2(self):
#     nono = Nonogram(test2)
#     self.assertEqual(nono.solve(), sol2)
#
#
# def test3(self):
#     nono = Nonogram(test3)
#     self.assertEqual(nono.solve(), sol3)
#

# NonogramTester().test_correct()

"""
my solution relies upon the correctness of the previous solution
if a clue is SOLVED it means there can be no other possibilities i.e it is solved 
relying on the validity of the previous solution means that a wrongly solved clue will affect the correctness of the nonogram
we assume it's correct so there can be no collisions and no mistakes

1. map each clue into Clue which maps the clue properties
    the clue itself
    it's type(row, col) it's index
    creates a list of possible solutions
    creates a always_black solution (cells that will always be 1 if any)
    a solution property
    a is_solved property
    
2. solving:
    a. start by looking for solved or no possibility clues
        if we can't find any create a list of clues sorted by the minimum possible solution count min to max
        call a recursive method that creates a new list of clues according to the current selected solution either solved or not
    b. mark clues with no possibilities i.e 1 solution as done
        i. if there
        if there are no "solved" clues loop over the possibilities start with the minimum
        
        i. if we found a single possible solution we mark the Clue as solved = True
        
    c. filter the opposing rows/cols by leaving only possible solutions
        i. create a new list of possible solutions per the selected clue 
        ii. if a single possibility is found mark it as the solution and the clue as solved
        iii. otherwise on
    
    

clue_mapp = {
    
    (4, ):  [[1, 1, 1, 1, 0], [0, 1, 1, 1, 1],
    (1, 3): [1, 0, 1, 1, 1],
    (3, 1): [1, 1, 1, 0, 1],
    (1, 1, 1): [1, 0, 1, 0, 1],
}

1.b use itertools combinations to calculate is it possible?

2. fill the always black into the solution matrix
    keep an index of used clues
    
3. run through the remaining clues in the order of smaller possibilities 
    i.e clues with the smallest number of possible values in the clue_map 
    to minimize checking
    
4. if we can't set the values we have to start over with the other possibilities 
    if we set values through the end return the solved nonogram
    if we tried all the possibilities and return a non solvable nonogram
    

"""
