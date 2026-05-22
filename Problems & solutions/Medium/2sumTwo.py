# Approach:
# Use two pointers starting at the beginning and end of the sorted array.
# If the sum is too large, move the right pointer left.
# If the sum is too small, move the left pointer right.
# Return the 1-based indices once the target sum is found.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]

            elif numbers[l] + numbers[r] > target:
                r -= 1

            else:
                l += 1
