# Approach:
# Use a max heap to always select the character with the highest remaining count.
# If adding that character would create three consecutive identical characters,
# temporarily use the second most frequent character instead. Reinsert characters
# back into the heap whenever they still have remaining occurrences.
#
# Time: O(a + b + c)
# Space: O(1)


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []

        if a:
            heap.append((a, "a"))
        if b:
            heap.append((b, "b"))
        if c:
            heap.append((c, "c"))

        heapq.heapify_max(heap)
        res = ""

        while heap:
            cnt, char = heapq.heappop_max(heap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not heap:
                    break
                # Getting second most common char
                cnt2, char2 = heapq.heappop_max(heap)
                cnt2 -= 1
                res += char2
                if cnt2:
                    heapq.heappush_max(heap, (cnt2, char2))

            else:
                res += char
                cnt -= 1
            if cnt:
                heapq.heappush_max(heap, (cnt, char))

        return res
