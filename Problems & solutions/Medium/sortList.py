# Approach:
# Traverse the linked list and store all node values in an array.
# Sort the array, then build a new linked list using the sorted values.
#
# Time: O(n log n)
# Space: O(n)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        arr = []

        curr = head

        while curr is not None:
            arr.append(curr.val)
            curr = curr.next

        arr.sort()

        newList = ListNode(0)
        curr = newList
        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next

        return newList.next