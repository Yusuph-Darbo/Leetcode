# Approach:
# Count the number of people who trust each person and the number of people
# each person trusts. The town judge is the person trusted by everyone else
# and who trusts nobody.
#
# Time: O(n + t)
# Space: O(n)


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for src, dst in trust:
            incoming[dst] += 1
            outgoing[src] += 1

        for i in range(1, n + 1):
            if incoming[i] == n - 1 and outgoing[i] == 0:
                return i

        return -1
