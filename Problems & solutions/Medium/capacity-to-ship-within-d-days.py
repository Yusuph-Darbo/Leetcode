# Approach:
# Use binary search on the ship's capacity. The minimum possible capacity is
# the heaviest package, and the maximum is the sum of all weights.
# For each candidate capacity, greedily load packages in order and count
# how many days are needed. If the required days are <= D, try a smaller
# capacity; otherwise, increase it.
#
# Time: O(n log(sum(weights) - max(weights)))
# Space: O(1)


class Solution:
    def shipWithinDays(self, weights: list[int], D: int) -> int:
        def feasible(capacity):
            days = 1
            total = 0
            for weight in weights:
                total += weight

                if total > capacity:
                    total = weight
                    days += 1
                    if days > D:
                        return False

            return True

        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2

            if feasible(mid):
                right = mid
            else:
                left = mid + 1

        return left
