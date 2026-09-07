# Approach:
# Use binary search to find a peak. If nums[mid] is greater than the next
# element, a peak exists on the left; otherwise, search the right half.
#
# Time: O(log n)
# Space: O(1)


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1

        return l
