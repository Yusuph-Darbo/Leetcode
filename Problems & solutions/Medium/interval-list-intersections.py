# Approach:
# Use two pointers to compare intervals from both lists. If two intervals
# overlap, append their intersection using the maximum start and minimum end.
# Advance the pointer belonging to the interval that ends first, since it
# cannot overlap with any future intervals in the other list.
#
# Time: O(m + n)
# Space: O(1) auxiliary space


class Solution:
    def intervalIntersection(
        self, firstList: list[list[int]], secondList: list[list[int]]
    ) -> list[list[int]]:
        i = 0
        j = 0

        res = []

        while i < len(firstList) and j < len(secondList):
            fStart, fEnd = firstList[i]
            sStart, sEnd = secondList[j]

            if fStart <= sEnd and sStart <= fEnd:
                res.append([max(fStart, sStart), min(fEnd, sEnd)])

            if fEnd <= sEnd:
                i += 1
            else:
                j += 1

        return res
