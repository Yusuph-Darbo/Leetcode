# Approach:
# Count the frequency of each number, then use a min-heap of size k to keep
# the k most frequent numbers.
#
# Time: O(n log k)
# Space: O(n)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        heap = []
        res = []

        for num, count in count.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)

        for count, num in heap:
            res.append(num)

        return res
