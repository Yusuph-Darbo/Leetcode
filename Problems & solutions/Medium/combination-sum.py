# Approach:
# Use backtracking to explore all combinations by deciding whether to
# include the current candidate or move to the next one. A candidate may
# be chosen multiple times, and recursion stops when the target is reached
# or exceeded.
#
# Time: Exponential
# Space: O(target)


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(candidates)

        def dfs(i, total):
            if total == target:
                res.append(sol.copy())
                return

            if total > target or i == n:
                return

            # Dont pick
            dfs(i + 1, total)

            # Pick
            sol.append(candidates[i])
            dfs(i, total + candidates[i])
            sol.pop()

        dfs(0, 0)

        return res
