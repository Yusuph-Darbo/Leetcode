# Approach:
# Separate and sort all meeting start and end times. Use two pointers to
# process events in chronological order: when a meeting starts, allocate a
# room; when a meeting ends, free a room. Track the maximum number of rooms
# in use at any time.
#
# Time: O(n log n)
# Space: O(n)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0
        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1

            res = max(res, count)

        return res
