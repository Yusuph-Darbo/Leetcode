# Approach:
# Generate permutations recursively by first finding all permutations of
# the remaining numbers. Then insert the current number into every possible
# position of each smaller permutation to build all permutations.
#
# Time: O(n! * n^2)
# Space: O(n! * n)


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perm = self.permute(nums[1:])
        res = []

        for p in perm:
            for i in range(len(p) + 1):
                pCopy = p.copy()
                pCopy.insert(i, nums[0])
                res.append(pCopy.copy())

        return res
