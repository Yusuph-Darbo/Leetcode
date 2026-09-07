# Approach:
# Sort intervals by start time and greedily keep the interval with the
# smallest end time when overlaps occur. This leaves the most room for
# future intervals and minimizes removals.
#
# Time: O(n log n)
# Space: O(1)


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)

        return res
