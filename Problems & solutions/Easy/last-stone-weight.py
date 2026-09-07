# Approach:
# Use a max heap to repeatedly retrieve the two heaviest stones.
# Smash them together and, if they are unequal, push the remaining
# weight back into the heap. Continue until at most one stone remains.
#
# Time: O(n log n)
# Space: O(n)


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            if first > second:
                heapq.heappush(stones, -(first - second))

        stones.append(0)
        return abs(stones[0])
