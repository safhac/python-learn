from typing import Optional


# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ln = 0
        tmp = head

        while tmp.next:
            ln = ln + 1
            tmp = tmp.next

        ln = ln // 2
        for i in range(ln):
            head = head.next  # type: ignore

        return head

    def middleNode2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head
        count = 0

        while head.next:
            head = head.next
            count += 1
            if count % 2 == 0:
                middle = middle.next
        if count % 2 == 1:
            middle = middle.next
        return middle


s = Solution()


def make_list(head, items):
    if items:
        head.next = ListNode(items[0])
        make_list(head.next, items[1:])


l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, 5, 6]
l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
h1 = ListNode(l3[0])
h2 = ListNode(l4[0])
make_list(h1, l3[1:])
make_list(h2, l4[1:])

r1 = Solution().middleNode2(h1)
r2 = Solution().middleNode2(h2)
#


def print_result(res):
    l = []
    while res.next:
        l.append(res.val)
        res = res.next

    l.append(res.val)
    print(l)


print_result(r1)
print_result(r2)

# if the list length is divisible return the latter 3 nodes
# if not divisible return the middle with two more
"""
one loop until reaching next=None
second loop until the middle returning it
"""

"""
 [1, 2, 3, 4, 5]
 middle = head
        count = 0
        
        while(head.next):
            head = head.next
            count += 1
            if count % 2 == 0:
                middle = middle.next
        if count % 2 ==1:
            middle = middle.next
        return middle
        
1. 
head.next = 2
head = head.next (2)
count += 1 (1)
2. 
head.next = 3
head (3)
count (2)
middle (2)
3. 
head.next = 4
head (4)
count (3)
middle (2)
4.
head.next = 5 
head (5)
count(4)
middle(3)
5.
head.next = None
head (5)
count(4)
middle(3)

"""
