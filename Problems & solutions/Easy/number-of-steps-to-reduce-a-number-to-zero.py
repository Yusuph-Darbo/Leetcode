# Approach:
# Repeatedly divide even numbers by 2 and subtract 1 from odd numbers until
# the number reaches 0, counting each operation.
#
# Time: O(log n)
# Space: O(1)


class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0

        while num > 0:
            if num % 2 == 0:
                count += 1
                num /= 2
            else:
                num -= 1
                count += 1
        return count
