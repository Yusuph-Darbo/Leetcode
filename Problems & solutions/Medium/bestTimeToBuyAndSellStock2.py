# Approach:
# Iterate through prices and accumulate profit whenever there is an increase
# from the previous day, effectively capturing all upward trends.
#
# Time: O(n)
# Space: O(1)


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit
