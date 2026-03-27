# Approach:
# Use binary search to find the minimum in a rotated sorted array.
# Compare the middle element with the rightmost element to decide the search space.
# If mid > high, the minimum lies in the right half; otherwise, it's in the left half (including mid).
# Continue until low meets high, which will point to the minimum element.
#
# Time: O(log n)
# Space: O(1)


class Solution:
    def findMin(self, nums: List[int]) -> int:

        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (high + low) // 2

            if nums[mid] > nums[high]:
                low = mid + 1

            else:
                high = mid

        return nums[low]
