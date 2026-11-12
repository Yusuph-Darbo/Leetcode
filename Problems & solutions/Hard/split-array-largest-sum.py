# Approach:
# Use binary search on the maximum allowed subarray sum. The minimum possible
# threshold is the largest element, and the maximum is the sum of all elements.
# For each candidate threshold, greedily split the array while keeping each
# subarray sum <= threshold. If at most k subarrays are needed, try a smaller
# threshold; otherwise, increase it.
#
# Time: O(n log(sum(nums) - max(nums)))
# Space: O(1)


class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def feasible(threshold):
            count = 1
            total = 0
            for num in nums:
                total += num

                if total > threshold:
                    total = num
                    count += 1
                    if count > k:
                        return False

            return True

        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2

            if feasible(mid):
                right = mid
            else:
                left = mid + 1

        return left
