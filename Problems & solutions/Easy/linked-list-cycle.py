# Approach:
# Traverse the linked list while storing visited nodes in a hash table.
# If we encounter a node that has already been seen, a cycle exists.
#
# Time: O(n)
# Space: O(n)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        table = {}
        curr = head

        while curr is not None:
            if curr.next in table:
                return True
            else:
                table[curr.next] = 0
                curr = curr.next

        return False
        