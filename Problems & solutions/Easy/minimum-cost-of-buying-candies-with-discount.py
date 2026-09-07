# Approach:
# Sort the candy costs in ascending order and process them
# from most expensive to least expensive. For every group
# of three candies, pay for the two most expensive and get
# the third one for free.
#
# Time: O(n log n)
# Space: O(1)


class Solution:
    def minimumCost(self, cost: List[int]) -> int:

        res = 0
        cost.sort()
        cnt = 0

        for i in range(len(cost) - 1, -1, -1):
            if cnt == 2:
                cnt = 0
                continue
            else:
                res += cost[i]
                cnt += 1

        return res
