# Approach:
# Sort the array, then fix one number and use two pointers to find the
# pair whose sum is closest to the target. Update the closest sum whenever
# a better candidate is found.
#
# Time: O(n^2)
# Space: O(1)


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if abs(target - total) < abs(target - res):
                    res = total

                if total == target:
                    return res

                elif total > target:
                    r -= 1

                else:
                    l += 1

        return res
