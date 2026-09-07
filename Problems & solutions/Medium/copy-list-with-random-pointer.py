# Approach:
# Create a copy of each node and store a mapping from original nodes to
# their corresponding copies. Then iterate through the original list again
# to assign the next and random pointers using the mapping. Return the copy
# of the head node.
#
# Time: O(n)
# Space: O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        # Map old nodes to new
        mapp = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            # Mapping old to copy
            mapp[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = mapp[curr]
            copy.next = mapp[curr.next]
            copy.random = mapp[curr.random]
            curr = curr.next

        return mapp[head]
