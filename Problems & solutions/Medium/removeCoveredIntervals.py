# Approach:
# Sort intervals by increasing start time and decreasing end time.
# Traverse the sorted intervals while tracking the largest end seen.
# If an interval extends beyond the current maximum end, count it;
# otherwise, it is covered by a previous interval.
#
# Time: O(n log n)
# Space: O(1)


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        res = 0
        maxEnd = -1

        for start, end in intervals:
            if end > maxEnd:
                res += 1
                maxEnd = end

        return res
