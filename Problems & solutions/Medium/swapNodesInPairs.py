# Approach:
# Use a dummy node that points to the head of the list.
# This helps handle edge cases where the head itself gets swapped.
#
# Time Complexity: O(n) 
# Space Complexity: O(1)


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummyNode = ListNode(0)
        dummyNode.next = head
        prev = dummyNode

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # Swapping the pair
            first.next = second.next
            prev.next = second
            second.next = first

            # next pair
            prev = first

        return dummyNode.next