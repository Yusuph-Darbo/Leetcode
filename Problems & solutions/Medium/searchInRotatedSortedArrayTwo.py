# Approach:
# Use binary search to determine which half of the rotated array is sorted.
# Handle duplicates by moving the left pointer when values are equal.
# Check if the target lies within the sorted half and discard the other half.
# Continue until the target is found or the search space is empty.
#
# Time: O(log n) average, O(n) worst case
# Space: O(1)


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return True

            while l < mid and nums[l] == nums[mid]:
                l += 1

            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False
