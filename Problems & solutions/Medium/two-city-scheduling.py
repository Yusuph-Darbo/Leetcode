# Approach:
# Sort people by the difference between the cost of flying to
# city A and city B. Send the first half to city A and the
# second half to city B to minimize the total cost.
#
# Time: O(n log n)
# Space: O(1)


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])

        n = len(costs) // 2
        res = 0

        for i in range(n):
            res += costs[i][0]

        for i in range(n, len(costs)):
            res += costs[i][1]

        return res
