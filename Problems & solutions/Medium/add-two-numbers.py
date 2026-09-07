# Approach:
# Create a dummy head node to simplify list construction.
#
# Use two pointers (p and q) to traverse both linked lists.
# Maintain a variable `carry` to store any overflow from addition.
#
# While either list still has nodes:
#   - Extract the current values from both lists (use 0 if a list is exhausted).
#   - Compute the sum of both values plus the carry.
#   - Update the carry (sum // 10).
#   - Create a new node with the digit (sum % 10) and attach it to the result list.
#
# After the loop, if a carry remains, append a final node.
#
# Return the next node after the dummy head (start of the result list).
#
# Time Complexity: O(N)
# Space Complexity: O(N)


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Make a new list
        # Transverse through the list while
        # either list has a valid next node
        newList = ListNode(0)
        p = l1
        q = l2
        curr = newList
        carry = 0

        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0

            value = carry + x + y
            carry = value // 10

            curr.next = ListNode(value % 10)
            curr = curr.next

            if p:
                p = p.next

            if q:
                q = q.next

        if carry > 0:
            curr.next = ListNode(carry)

        return newList.next