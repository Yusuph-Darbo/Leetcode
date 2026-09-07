# Approach:
# Iterate from 3 to n and add each number that is divisible by 3, 5, or 7.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        total = 0

        for i in range(3, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                total += i

        return total
