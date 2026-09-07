# Approach:
# Extract each digit using modulo and integer division. Track the product
# and sum of the digits, then return their difference.
#
# Time: O(log n)
# Space: O(1)


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total = 0

        while n > 0:
            product *= n % 10
            total += n % 10

            n //= 10

        return product - total
