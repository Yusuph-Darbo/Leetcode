# Approach:
# Build the running sum by adding each number to the previous cumulative sum.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        results = [0] * len(nums)
        results[0] = nums[0]

        for i in range(1, len(nums)):
            results[i] = nums[i] + results[i - 1]

        return results
