# Approach:
# Use backtracking to explore every possible subset by deciding whether to
# include or exclude each element. When all elements have been considered,
# add the current subset to the result.
#
# Time: O(2^n)
# Space: O(n)


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        def backtrack(i):
            if i == n:
                # Returns a copy
                res.append(sol[:])
                return

            # Dont pick
            backtrack(i + 1)

            # Pick
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

        backtrack(0)

        return res
