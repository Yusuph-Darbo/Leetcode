# Approach:
# Sort the people by weight and use two pointers.
# Pair the lightest and heaviest person whenever possible;
# otherwise, send the heaviest person alone in a boat.
#
# Time: O(n log n)
# Space: O(1)


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        cnt = 0
        l, r = 0, len(people) - 1

        while l <= r:
            if people[l] + people[r] > limit:
                r -= 1
            else:
                l += 1
                r -= 1

            cnt += 1

        return cnt
