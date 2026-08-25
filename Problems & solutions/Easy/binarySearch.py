# Approach:
# Use binary search on the sorted array. Compare the middle element with
# the target and eliminate half of the search space each iteration.
#
# Time: O(log n)
# Space: O(1)


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                l = mid + 1

            else:
                r = mid - 1

        return -1
