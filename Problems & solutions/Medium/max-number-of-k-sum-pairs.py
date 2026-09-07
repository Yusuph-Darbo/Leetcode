# Approach:
# Sort the array and use two pointers from both ends.
# If the current pair sums to k, count the operation and
# move both pointers. Otherwise, adjust the pointers based
# on whether the sum is too large or too small.
#
# Time: O(n log n)
# Space: O(1)


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        res = 0

        nums.sort()

        while l < r:
            total = nums[l] + nums[r]

            if total == k:
                res += 1
                l += 1
                r -= 1

            elif total > k:
                r -= 1
            else:
                l += 1

        return res
