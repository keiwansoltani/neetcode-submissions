"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        NewCopy = {None:None}
        curr = head
        while curr:
            copy=Node(curr.val)
            NewCopy[curr] = copy
            curr=curr.next
        curr = head
        while curr:
            copy = NewCopy[curr]
            copy.next = NewCopy[curr.next]
            copy.random = NewCopy[curr.random]
            curr = curr.next
        return NewCopy[head]