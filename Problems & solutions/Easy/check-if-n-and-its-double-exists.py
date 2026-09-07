# Approach:
# Use a set to track previous values. For each number, check whether its
# double or half has already been seen.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()

        for i in arr:
            if i * 2 in seen or i / 2 in seen:
                return True
            seen.add(i)

        return False
