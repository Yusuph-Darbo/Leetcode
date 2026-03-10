# Approach:
# Use binary search to find the target in the sorted array.
# If the target is not found, return the index where it should
# be inserted to maintain the sorted order.
#
# Time: O(log n)
# Space: O(1)

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        if nums[mid] < target:
            return mid + 1

        return mid