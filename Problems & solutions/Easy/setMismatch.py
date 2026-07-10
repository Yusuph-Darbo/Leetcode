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
