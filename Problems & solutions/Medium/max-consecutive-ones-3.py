# Approach:
# Use a sliding window containing at most k zeros. Expand the window by moving
# right, and shrink it from the left whenever the zero count exceeds k.
# Track the maximum valid window length.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left, maxLength, zeroCount = 0, 0, 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1
            while zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)

        return maxLength
