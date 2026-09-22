# Approach:
# Build two linked lists: one for nodes with values less than x and one for
# the remaining nodes. Then connect the two lists while preserving their order.
#
# Time: O(n)
# Space: O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        small_list = ListNode()
        big_list = ListNode()

        small = small_list
        big = big_list

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next

            head = head.next

        small.next = big_list.next
        big.next = None

        return small_list.next
