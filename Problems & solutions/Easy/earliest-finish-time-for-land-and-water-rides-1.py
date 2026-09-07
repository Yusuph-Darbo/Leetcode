# Approach:
# Find the earliest finish time for any land ride and any water ride.
# Try doing land first, then each water ride, and water first,
# then each land ride, updating the minimum possible finish time.
#
# Time: O(n + m)
# Space: O(1)


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        minL = float("inf")
        minW = float("inf")
        res = float("inf")
        n = len(landStartTime)
        m = len(waterStartTime)

        for i in range(n):
            minL = min(minL, landStartTime[i] + landDuration[i])

        for i in range(m):
            minW = min(minW, waterStartTime[i] + waterDuration[i])
            res = min(res, max(minL, waterStartTime[i]) + waterDuration[i])

        for i in range(n):
            res = min(res, max(minW, landStartTime[i]) + landDuration[i])

        return res
