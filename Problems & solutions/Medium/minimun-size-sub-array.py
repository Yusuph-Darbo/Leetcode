# Approach:
# Use a sliding window to maintain a running sum.
# Expand right to increase the sum; shrink left while sum >= target.
# Update the minimum window length each time the condition is met.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = left = 0
        res = float("inf")

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if res == float("inf") else res
