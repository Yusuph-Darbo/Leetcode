# Approach:
# Use Python's built-in exponentiation operator (**) to compute x raised to the power n.
#
# Time: O(log n)
# Space: O(1)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        return x ** n
        