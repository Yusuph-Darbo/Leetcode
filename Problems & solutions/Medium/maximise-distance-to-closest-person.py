# Approach:
# Track the previous occupied seat. Update the maximum distance using the
# leading gap, half the gap between occupied seats, and the trailing gap.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        res = 0
        prev = -1

        for i, seat in enumerate(seats):
            if seat == 1:
                if prev == -1:
                    res = i
                else:
                    res = max(res, (i - prev) // 2)

                prev = i

        res = max(res, len(seats) - 1 - prev)

        return res
