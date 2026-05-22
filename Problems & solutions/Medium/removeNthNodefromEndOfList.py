# Approach:
# Use two pointers with a dummy node. Move the first pointer n+1 steps
# ahead, then move both pointers together until the first reaches the end.
# The second pointer will be just before the node to remove.
#
# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0, head)
        curr = dummy
        prev = dummy

        for i in range(n + 1):
            curr = curr.next

        while curr:
            curr = curr.next
            prev = prev.next

        prev.next = prev.next.next

        return dummy.next