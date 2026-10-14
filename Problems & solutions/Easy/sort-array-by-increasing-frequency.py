# Approach:
# Count each number's frequency, then use a min-heap ordered by frequency
# and descending value to output numbers from least to most frequent.
#
# Time: O(n + m log m)
# Space: O(n)


class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        count = {}
        minHeap = []
        res = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for num, count in count.items():
            heapq.heappush(minHeap, [count, -num])

        while minHeap:
            freq, count = heapq.heappop(minHeap)

            for _ in range(freq):
                res.append(-count)

        return res
