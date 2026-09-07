# Approach:
# Use two pointers to traverse both sorted linked lists.
# At each step, append the smaller value to a new list and move that pointer forward.
# After one list is exhausted, append the remaining nodes from the other list.
#
# Time: O(n + m)
# Space: O(n + m)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode(0)
        curr = head
        ptr1 = list1
        ptr2 = list2

        while ptr1 and ptr2:
            if ptr1.val > ptr2.val:
                curr.next = ListNode(ptr2.val)
                ptr2 = ptr2.next

            else:
                curr.next = ListNode(ptr1.val)
                ptr1 = ptr1.next

            curr = curr.next

        while ptr1:
            curr.next = ListNode(ptr1.val)
            ptr1 = ptr1.next
            curr = curr.next

        while ptr2:
            curr.next = ListNode(ptr2.val)
            ptr2 = ptr2.next
            curr = curr.next
        
        
        return head.next