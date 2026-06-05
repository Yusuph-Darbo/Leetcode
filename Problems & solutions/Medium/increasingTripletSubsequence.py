# Approach:
# Track the smallest and second smallest values seen so far.
# If a number is found that is greater than both, an increasing
# triplet subsequence exists and can be returned immediately.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float("inf")
        second = float("inf")

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                print(first, second)
                return True
        return False
