# Approach:
# Use memoized recursion to compare skipping the current house with robbing it
# and skipping the next house. Store each result to avoid repeated calculations.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def rob(self, nums: list[int]) -> int:
        memo = {}

        def dfs(i):
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))

            return memo[i]

        return dfs(0)
