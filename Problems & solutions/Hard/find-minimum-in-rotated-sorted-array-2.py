# Approach:
# Use modified binary search to find the minimum in a rotated sorted array
# that may contain duplicates. Compare the middle element with the rightmost:
# keep the left half if nums[mid] < nums[r], discard the left half if
# nums[mid] > nums[r], and shrink r by one when they are equal.
#
# Time: O(log n) average, O(n) worst case with duplicates
# Space: O(1)


class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            # duplicate
            else:
                r -= 1

        return nums[l]
