# Approach:
# Use Kadane's algorithm. At each number, decide whether to start a new
# subarray or extend the current one, while tracking the best sum found.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = nums[0]
        total = 0

        for num in nums:
            total = max(num, total + num)
            res = max(total, res)

        return res
