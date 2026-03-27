# Approach:
# Treat the array as a linked list where each index points to nums[index].
# Use Floyd’s Cycle Detection (Tortoise and Hare) to find the intersection point.
# Reset one pointer to the start and move both one step at a time to find the cycle entry (duplicate).
#
# Time: O(n)
# Space: O(1)


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(fast)
            if slow == fast:
                break

        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
