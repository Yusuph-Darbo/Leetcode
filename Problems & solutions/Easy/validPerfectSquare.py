# Approach:
# Use Newton's method to repeatedly improve an estimate of the square root.
# Stop when the estimate is no longer too large, then check if its square
# equals num.
#
# Time: O(log n)
# Space: O(1)


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = num
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num
