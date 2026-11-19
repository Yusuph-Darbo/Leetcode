# Approach:
# Reverse the integer digit by digit using remainder and division.
# Before adding each digit, check whether multiplying the current result
# by 10 and adding the digit would exceed the 32-bit signed integer range.
# Return 0 if the reversed integer overflows.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def reverse(self, x: int) -> int:
        minRange = -(2**31)
        maxRange = 2**31 - 1

        res = 0

        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            # out of the higher range
            if res > maxRange // 10 or (res == maxRange and digit >= maxRange % 10):
                return 0

            # out of the lower range
            if res < minRange // 10 or (
                res == minRange // 10 and digit <= minRange % 10
            ):
                return 0

            res = res * 10 + digit

        return res
