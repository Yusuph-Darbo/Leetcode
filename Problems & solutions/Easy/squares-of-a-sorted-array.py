# Approach:
# Use two pointers at both ends of the sorted array. Compare the absolute
# values, place the larger square at the end of the result, and move the
# corresponding pointer inward.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * length
        left, right = 0, length - 1
        pos = length - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] ** 2
                left += 1
            else:
                result[pos] = nums[right] ** 2
                right -= 1
            pos -= 1

        return result
