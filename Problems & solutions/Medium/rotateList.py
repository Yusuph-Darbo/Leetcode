# Approach:
# Store all node values in an array, rotate the array using
# (i + k) % n to compute the new index, then build a new
# linked list using the rotated values.
#
# Time: O(n)
# Space: O(n)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        arr = []

        curr = head
        while curr is not None:
            arr.append(curr.val)
            curr = curr.next

        n = len(arr)
        rotatedArr = [0] * len(arr)

        for i in range(n):
            rotatedArr[(i + k) % n] = arr[i]

        newList = ListNode(0)
        curr = newList

        for num in rotatedArr:
            curr.next = ListNode(num)
            curr = curr.next

        return newList.next
            