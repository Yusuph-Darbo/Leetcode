# Approach:
# Use a dummy node pointing to the head to handle edge cases.
#
# Use two pointers:
# prev — tracks the last node that is confirmed unique
# temp — traverses the list
#
# If duplicates are found, skip all nodes with that value.
# Link prev.next to the next non-duplicate node.
#
# If no duplicate, move both pointers forward.
#
# Return dummy.next as the new head.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Make a extra node that points to head
        dummy = ListNode(0, head)

        prev = dummy
        temp = head

        # Iterate thorugh the list
        while temp:

            if temp.next and temp.val == temp.next.val:
                # Skip all duplicates
                while temp and temp.val == prev.next.val:
                    temp = temp.next
                prev.next = temp
            else:
                prev = temp
                temp = temp.next

        return dummy.next