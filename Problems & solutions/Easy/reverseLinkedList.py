# Approach:
# Reverse the linked list iteratively by updating the next pointer of each node.
# Keep track of the previous node (prev) and move through the list with curr,
# reversing the links one node at a time until the list is fully reversed.
#
# Time Complexity: O(n)
# Space Complexity: O(1) 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # I can iterate through the linked list 
        # And store each value in an arr

        prev = None
        curr = head

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev