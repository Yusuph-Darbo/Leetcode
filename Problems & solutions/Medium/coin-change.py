# Approach:
# Use bottom-up dynamic programming where memo[a] stores the minimum coins
# needed to make amount a. Try each coin and keep the minimum valid count.
#
# Time: O(amount * len(coins))
# Space: O(amount)


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        memo = [float("inf")] * (amount + 1)
        memo[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    memo[a] = min(memo[a], 1 + memo[a - c])

        return memo[amount] if memo[amount] != float("inf") else -1
