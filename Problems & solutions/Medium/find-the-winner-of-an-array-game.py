# Approach:
# Track the current winner and their consecutive win streak. Each new element
# is the next challenger. If it beats the current winner, reset the streak;
# otherwise, increment it. Stop once the streak reaches k.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:
        cur = arr[0]
        win = 0

        for i in range(1, len(arr)):
            if arr[i] > cur:
                cur = arr[i]
                win = 0
            win += 1
            if win == k:
                break

        return cur
