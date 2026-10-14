# Approach:
# Use binary search to find where the new interval belongs, insert it, then
# merge overlapping intervals in a single pass.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        if not intervals:
            return [newInterval]

        n = len(intervals)
        l, r = 0, n - 1
        target = newInterval[0]

        while l <= r:
            mid = l + (r - l) // 2

            if intervals[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1

        intervals.insert(l, newInterval)

        res = []

        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])

        return res
