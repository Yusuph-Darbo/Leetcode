# Approach:
# Sort meetings by their start time and compare each meeting with the
# previous one. If a meeting starts before the previous meeting ends,
# an overlap exists and all meetings cannot be attended.
#
# Time: O(n log n)
# Space: O(1)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda i: i.start)
        prev = [intervals[0].start, intervals[0].end]

        for interval in intervals[1:]:
            if interval.start < prev[1]:
                return False
            else:
                prev = [interval.start, interval.end]

        return True
