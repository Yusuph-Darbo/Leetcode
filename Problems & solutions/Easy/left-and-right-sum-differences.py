# Approach:
# Build prefix and suffix sums for each position, then calculate the
# absolute difference between the sums on the left and right.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        pre = [1] * n
        suf = [1] * n

        pre[0] = suf[-1] = 0

        for i in range(1, n):
            pre[i] = nums[i - 1] + pre[i - 1]

        for i in range(n - 2, -1, -1):
            suf[i] = nums[i + 1] + suf[i + 1]

        for i in range(n):
            res[i] = abs(pre[i] - suf[i])

        return res
