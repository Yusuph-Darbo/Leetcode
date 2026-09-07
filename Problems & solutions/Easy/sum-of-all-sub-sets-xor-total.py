# Approach:
# Use backtracking to explore every subset by deciding whether to include
# each number. Keep track of the current XOR value, and when a complete
# subset is formed, add its XOR to the final sum.
#
# Time: Exponential
# Space: O(n)


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)

        def dfs(i, total):
            if i == n:
                return total

            return dfs(i + 1, total ^ nums[i]) + dfs(i + 1, total)

        return dfs(0, 0)
