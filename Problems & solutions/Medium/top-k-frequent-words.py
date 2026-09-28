# Approach:
# Count each word's frequency, then use a heap ordered by negative frequency
# and alphabetically by word to extract the k most frequent words.
#
# Time: O(n + m log m)
# Space: O(m)


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        minHeap = []
        count = {}
        res = []

        for word in words:
            count[word] = 1 + count.get(word, 0)

        for word, count in count.items():
            heapq.heappush(minHeap, (-count, word))

        while minHeap and k > 0:
            count, word = heapq.heappop(minHeap)
            res.append(word)
            k -= 1

        return res
