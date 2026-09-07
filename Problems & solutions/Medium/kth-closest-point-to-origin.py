# Approach:
# Maintain a max heap of size k containing the closest points seen so far.
# For each point, compute its squared distance from the origin and add it
# to the heap. If the heap exceeds size k, remove the farthest point.
#
# Time: O(n log k)
# Space: O(k)


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # I create a max heap with limit k
        maxHeap = []
        res = []

        for x, y in points:
            dist = x**2 + y**2

            heapq.heappush_max(maxHeap, (dist, [x, y]))

            if len(maxHeap) > k:
                heapq.heappop_max(maxHeap)

        for _, point in maxHeap:
            res.append(point)

        return res
