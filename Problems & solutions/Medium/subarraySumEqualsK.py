# Approach:
# Use a running prefix sum and a hashmap to track how many times each
# prefix sum has occurred. For each position, check if (current_sum - k)
# exists in the hashmap, as this indicates a subarray ending at the current
# index whose sum equals k.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur = 0
        prefixSum = {0: 1}

        for n in nums:
            cur += n
            diff = cur - k

            res += prefixSum.get(diff, 0)
            prefixSum[cur] = 1 + prefixSum.get(cur, 0)

        return res
