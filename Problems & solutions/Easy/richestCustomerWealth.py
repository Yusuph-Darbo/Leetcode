# Approach:
# Calculate the total wealth of each customer and return the maximum value.
#
# Time: O(m * n)
# Space: O(m)


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(acc) for acc in accounts])
