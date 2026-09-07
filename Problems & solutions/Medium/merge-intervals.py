# Approach:
# Sort intervals by their start time. Iterate through the sorted intervals,
# merging overlapping intervals by extending the end of the current interval.
# When no overlap exists, add the current interval to the result and start
# tracking a new interval.
#
# Time: O(n log n)
# Space: O(n)


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]
        res = []

        for start, end in intervals[1:]:
            if start <= prev[1]:
                prev[1] = max(prev[1], end)
            else:
                res.append(prev)
                prev = [start, end]

        res.append(prev)

        return res
