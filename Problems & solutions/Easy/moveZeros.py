# Approach:
# Use two pointers: left and right, both starting at index 0.
#
# The right pointer scans through the entire array.
# Whenever a non-zero element is found at right, swap it with the element at left.
#
# This moves all non-zero elements toward the front of the array,
# while zeroes naturally move toward the end.
#
# After swapping, increment left to point to the next position for a non-zero element.
# Always increment right to continue scanning the array.
#
# This modifies the array in place without using extra space.
#
# Time Complexity: O(n) — each element is visited once.
# Space Complexity: O(1) — no extra space is used.


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = 0

        while right < len(nums):
            if nums[right] != 0:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp

                left +=1
            
            right += 1