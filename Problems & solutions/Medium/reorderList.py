# Approach:
# Use fast and slow pointers to find the middle of the linked list.
# Reverse the second half of the list in-place.
# Merge the first half and reversed second half by alternating nodes.
#
# Time: O(n)
# Space: O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = head.next
        slow = head

        # Gets mid point
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse 2nd half
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
