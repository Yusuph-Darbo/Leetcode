# Approach:
# Count the occurrences of every number from 1 to n using a hashmap.
# Then identify the duplicated number (count of 2) and the missing
# number (count of 0) by scanning the frequency map.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mapp = {i: 0 for i in range(1, n + 1)}

        for n in nums:
            mapp[n] += 1

        dup, miss = 0, 0

        for key, val in mapp.items():
            if val == 2:
                dup = key
            if val == 0:
                miss = key

        return [dup, miss]
