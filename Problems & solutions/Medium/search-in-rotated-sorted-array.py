# Approach:
# Use binary search to determine which half of the rotated array is sorted.
# Check if the target lies within the sorted half and discard the other half.
# Repeat until the target is found or the search space is empty.
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

            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
