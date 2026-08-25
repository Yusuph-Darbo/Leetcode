# Approach:
# Repeatedly divide n by 3 while it is divisible by 3. If it reaches 1,
# n is a power of three; otherwise, return False.
#
# Time: O(log n)
# Space: O(1)


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n >= 0:
            if n == 1:
                return True
            elif n == 0:
                return False
            elif n % 3 != 0:
                return False
            n //= 3
        return False
