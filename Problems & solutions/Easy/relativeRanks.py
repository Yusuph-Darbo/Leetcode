# Approach:
# Use a max heap to process athletes in descending order of score.
# Assign medal names to the top three athletes and numerical ranks
# to the remaining athletes while preserving their original indices.
#
# Time: O(n log n)
# Space: O(n)


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []

        # Creates a max heap sorted by score
        for i, s in enumerate(score):
            heapq.heappush(heap, (-s, i))

        res = [""] * len(score)
        rank = 1

        while heap:
            _, i = heapq.heappop(heap)

            if rank == 1:
                res[i] = "Gold Medal"
            elif rank == 2:
                res[i] = "Silver Medal"
            elif rank == 3:
                res[i] = "Bronze Medal"
            else:
                res[i] = str(rank)

            rank += 1

        return res
