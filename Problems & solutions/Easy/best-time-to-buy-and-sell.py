# Approach:
# Traverse the array once while tracking:
# - The minimum price seen so far (best buying opportunity)
# - The maximum profit achievable at each step
#
# For each price:
# - If it is lower than the current minimum price, update the minimum.
# - Otherwise, calculate the profit if we sold at this price
#   (current price - minimum price so far).
# - Update the maximum profit if this profit is larger.
#
#
# Time Complexity: O(n) — we scan the array once.
# Space Complexity: O(1) — only two variables are used.


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = prices[0]
        maxPrice = 0

        for price in prices:
            if price < minPrice:
              minPrice = price   
            else: 
                profit = price - minPrice
                maxPrice = max(maxPrice, profit)

        return maxPrice