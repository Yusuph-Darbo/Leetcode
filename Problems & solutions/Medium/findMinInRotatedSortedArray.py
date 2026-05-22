# Approach:
# Use binary search to find the minimum in the rotated sorted array.
# If the current range is already sorted, the leftmost value is the minimum.
# Otherwise, check the middle element and discard the sorted half.
# Track the smallest value seen during the search.
#
# Time: O(log n)
# Space: O(1)


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = l + (r - l) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1

            else:
                r = mid - 1

        return res
