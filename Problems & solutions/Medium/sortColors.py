# Approach:
# Use the Dutch National Flag algorithm with three pointers:
# - low:  position where the next 0 should go
# - mid:  current element being examined
# - high: position where the next 2 should go
#
# Traverse the array once:
# - If nums[mid] == 0, swap it with nums[low] and move both pointers forward.
# - If nums[mid] == 1, it is already in the correct region, so just move mid.
# - If nums[mid] == 2, swap it with nums[high] and move high backward
#   (do NOT move mid yet, because the swapped value must be checked).
#
#
# Time Complexity: O(n) — each element is processed at most once.
# Space Complexity: O(1) — sorting is done in-place using only pointers.


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                # Swapping the values of the low and mid pointers
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1