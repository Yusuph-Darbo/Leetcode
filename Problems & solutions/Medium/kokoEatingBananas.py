# Approach:
# Use binary search on the possible eating speeds from 1 to max(piles).
# For each speed, calculate the total hours needed to eat all piles.
# If the speed works within h hours, try a smaller speed.
# Otherwise, search for a larger speed.
#
# Time: O(n log m)
# Space: O(1)
# where m is the maximum pile size.


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = l + (r - l) // 2
            hours = 0

            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res
