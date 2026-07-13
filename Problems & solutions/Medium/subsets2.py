# Approach:
# Sort the array, then use backtracking to generate all subsets by deciding
# whether to include each element. Skip consecutive duplicate values when
# excluding an element to avoid generating duplicate subsets.
#
# Time: O(n * 2^n)
# Space: O(n)


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, sol = [], []
        n = len(nums)

        def backtrack(i):
            if i == n:
                res.append(sol.copy())
                return

            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1

            backtrack(i + 1)

        backtrack(0)

        return res
