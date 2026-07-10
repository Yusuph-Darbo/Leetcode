# Approach:
# Use backtracking to explore all possible selections by deciding whether
# to include each number from 1 to n. When all numbers have been considered,
# add the current combination if it contains exactly k elements.
#
# Time: Exponential
# Space: O(n)


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, sol = [], []

        def dfs(i):
            if i > n:
                if len(sol) == k:
                    res.append(sol.copy())
                return

            dfs(i + 1)

            sol.append(i)
            dfs(i + 1)
            sol.pop()

        dfs(1)

        return res
