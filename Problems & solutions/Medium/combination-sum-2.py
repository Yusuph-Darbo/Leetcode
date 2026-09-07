# Approach:
# Sort the array, then use backtracking to explore all combinations by
# choosing or skipping each number. Skip consecutive duplicates when
# excluding a number to avoid generating duplicate combinations.
#
# Time: O(n * n^2)
# Space: O(n)


class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)
        nums.sort()

        def backtrack(i, total):
            if total == target:
                res.append(sol.copy())
                return

            if total > target or i == n:
                return

            # Pick
            sol.append(nums[i])
            backtrack(i + 1, total + nums[i])
            sol.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # Dont pick
            backtrack(i + 1, total)

        backtrack(0, 0)

        return res
