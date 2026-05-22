# Approach:
# First, check if the target exists in the array.
# Use binary search to find the leftmost (first) occurrence of the target.
# Then, use a second binary search (right-biased) to find the rightmost (last) occurrence.
# Return the starting and ending indices of the target.
#
# Time: O(log n)
# Space: O(1)


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]

        low = 0
        high = len(nums) - 1

        res = []

        while low < high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid

        res.append(low)

        high = len(nums) - 1

        while low < high:
            # Bias the right side
            mid = (low + high) // 2 + 1

            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid

        res.append(high)

        return res
