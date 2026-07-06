# Approach:
# Separate the list into odd- and even-indexed nodes by updating pointers
# in place. After processing all nodes, connect the end of the odd list
# to the head of the even list.
#
# Time: O(n)
# Space: O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd, even = head, head.next
        evenHead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenHead

        return head
