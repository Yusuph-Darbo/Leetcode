# Approach:
# First count the number of nodes to find the middle index.
# Traverse to the node just before the middle, then remove
# the middle node by skipping it.
#
# Time: O(n)
# Space: O(1)


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not head or not head.next:
            return None

        length = 0
        curr = head

        while curr is not None:
            length += 1
            curr = curr.next

        curr = head

        middle = length // 2

        for _ in range(middle - 1):
            curr = curr.next

        curr.next = curr.next.next

        return head
