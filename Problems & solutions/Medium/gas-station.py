# Approach:
# If total gas is less than total cost, completing the circuit is impossible.
# Otherwise, track the current fuel balance and reset the starting point
# whenever the balance becomes negative.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                res = i + 1

        return res
