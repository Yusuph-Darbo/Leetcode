# Approach:
# Sort the array to enable the two-pointer technique.
# Fix one element and use two pointers to find pairs that sum to the negative of the fixed element.
# Move pointers based on the sum and skip duplicates to avoid repeated triplets.
# Collect all unique triplets that sum to zero.
#
# Time: O(n^2)
# Space: O(1) (excluding output)


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        arr = []
        nums.sort()

        for i in range(len(nums)):
            # If they are the same move i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1

                elif total < 0:
                    j += 1

                else:
                    arr.append([nums[i], nums[j], nums[k]])
                    j += 1

                    # Avoids duplicate triplets
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return arr
