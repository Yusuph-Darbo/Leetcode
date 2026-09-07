# Approach:
# Use logarithms to check whether n has an integer exponent when expressed
# as a power of 4. Return False for non-positive values.
#
# Time: O(1)
# Space: O(1)


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        return math.log(n, 4).is_integer()
