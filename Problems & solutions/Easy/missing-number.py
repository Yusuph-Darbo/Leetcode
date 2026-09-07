# Approach:
# Calculate the expected sum of numbers from 0 to n and subtract the sum
# of the given numbers to find the missing value.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ExpectedValue = 0
        AccValue = 0
        for i in range(len(nums)):
            AccValue += nums[i]
            ExpectedValue += i + 1

        return ExpectedValue - AccValue
