# Approach:
# Use bottom-up dynamic programming. cache[i] stores the length of the
# longest increasing subsequence starting at index i. Iterate backwards and
# check every later element to extend the subsequence when nums[i] < nums[j].
#
# Time: O(n^2)
# Space: O(n)


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        cache = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    cache[i] = max(cache[i], 1 + cache[j])

        return max(cache)
