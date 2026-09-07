# Approach:
# Build the Fibonacci sequence iteratively, storing each value in an array.
# Return the nth value after constructing the sequence.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        total = [0, 1]

        for i in range(1, n):
            total.append(total[i] + total[i - 1])
        return total[n]
