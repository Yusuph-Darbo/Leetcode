# Approach:
# First count the number of nodes in the linked list, then traverse
# again to the index n // 2 to return the middle node.
#
# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        nodeCount = 0
        curr = head

        while curr is not None:
            curr = curr.next
            nodeCount += 1

        curr = head
        node = nodeCount // 2

        for i in range(node):
            curr = curr.next

        return curr