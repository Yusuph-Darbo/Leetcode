# Approach:
# Use two pointers, ptrA and ptrB, starting at the heads of list A and list B.
#
# Traverse both lists simultaneously.
# When ptrA reaches the end of list A, redirect it to the head of list B.
# When ptrB reaches the end of list B, redirect it to the head of list A.
#
# This ensures both pointers travel the same total distance:
# lengthA + lengthB.
#
# If the lists intersect, the pointers will meet at the intersection node.
# If the lists do not intersect, both pointers will eventually become None.
#
# Return the node where both pointers meet.
#
# Time Complexity: O(n + m) — each list is traversed at most twice.
# Space Complexity: O(1) — no extra space is used.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        # Make both list pointers travel the same distance 
        ptrA = headA
        ptrB = headB

        while ptrA != ptrB:
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA

        return ptrA