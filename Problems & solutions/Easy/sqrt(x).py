# Approach:
# Use binary search to find the largest number whose square is less than
# or equal to x. Return the right pointer when the search ends.
#
# Time: O(log n)
# Space: O(1)


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l, r = 1, x // 2

        while l <= r:
            mid = l + (r - l) // 2
            sqr = mid * mid

            if sqr == x:
                return mid
            elif sqr > x:
                r = mid - 1
            else:
                l = mid + 1

        return r
