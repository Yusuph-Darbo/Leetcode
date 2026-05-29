# Approach:
# Compute the sum of digits for each number in the array.
# Keep track of the smallest digit sum encountered and
# return it after processing all numbers.
#
# Time: O(n * d)
# Space: O(1)
# where d is the number of digits in a number.


class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = float("inf")

        for num in nums:
            total = 0
            while num > 0:
                digit = num % 10
                total += digit
                num = num // 10

            res = min(total, res)

        return res
