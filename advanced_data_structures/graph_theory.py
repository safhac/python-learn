"""
depth first search
DFS
------------------------------------------------------------------------
breadth first search
BFS
------------------------------------------------------------------------

lowest common ancestor
LCA

given two nodes in a tree, what is their lowest common ancestor
                    1
                  /   \
                2       3
              /       /
            6       4
          /   \      \
        8       7     5

step:       0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14
euler tour: 1, 2, 6, 8, 6, 7, 6, 2, 1, 3, 4, 5, 4, 3, 1
depth:      0, 1, 2, 3, 2, 3, 2, 1, 0, 1, 2, 3, 2 ,1, 0

depth[i] = depth of node i

LCA(a, b) = min(depth[euler[first a]], ..., depth[euler[first b]])
i.e the minimum depth of all nodes from the 1st occurrence of a through the euler tour until the 1st occurrence of b

example:
find the lowest ancestor of euler[3] = 8, euler[5] = 7
depth[8] = 3, depth[7] = 3, first occurrence of 8 = 3, first occurrence of 7 = 5
min(depth[euler[3]], depth[euler[4]], depth[euler[5]]) = node 6

"""
from random import randint
import numpy as np

inf = 10 ** 20


class Node:
    def __init__(self, label, children=None, parent=None):
        self.label = label
        self.children = children if children else []
        self.parent = parent


def euler_tour(node):
    if not node.children:
        return [node.label]

    result = [node.label]
    for child in node.children:
        result.extend(euler_tour(child))
        result.append(node.label)
    return result


def get_depths(node):
    depth = {}

    def inner(node, d):
        depth[node.label] = d
        for child in node.children:
            inner(child, d + 1)

    inner(node, 0)
    return depth


def get_possitions(euler):
    position = {}
    for i, v in enumerate(euler):
        if v not in position:
            position[v] = i

        return position


def query(array, segment_tree, a, b):
    def inner(node, left, right):
        if right < a or left > b:
            return None
        if a <= left and right <= b:
            return segment_tree[node]
        m = (left + right) // 2
        l_res = inner(2 * node + 1, left, m)
        r_res = inner(2 * node + 2, m + 1, right)
        if l_res is None:
            return r_res
        if r_res is None:
            return l_res
        if array[l_res] < array[r_res]:
            return l_res
        return r_res
    return inner(0, 0, len(array) - 1)


head = Node(1, [Node(2, [Node(6, [Node(8), Node(7)])]), Node(3, [Node(4, [Node(5)])])])
et = euler_tour(head)
print(et)
print(get_possitions(et))
print(get_depths(head))
