# Approach:
# Sort the array and use two pointers. If the smallest and largest values
# have a sum below target, every value between them also forms a valid pair.
#
# Time: O(n log n)
# Space: O(1)


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1

        return count
