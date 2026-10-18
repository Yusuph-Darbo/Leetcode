# Approach:
# Use memoized recursion to store previously calculated Fibonacci numbers,
# avoiding repeated calculations.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def fib(self, n: int) -> int:
        memo = {0: 0, 1: 1}

        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = f(x - 2) + f(x - 1)
                return memo[x]

        return f(n)
