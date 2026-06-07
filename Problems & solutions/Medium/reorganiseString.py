# Approach:
# Count the frequency of each character and store them in a max heap.
# Repeatedly choose the most frequent available character while keeping
# the previously used character out of the heap for one step to avoid
# adjacent duplicates.
#
# Time: O(n log k)
# Space: O(k)
# where k is the number of distinct characters.


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [(cnt, val) for val, cnt in count.items()]
        res = ""
        prev = None

        heapq.heapify_max(heap)

        while heap or prev:
            if prev and not heap:
                return ""

            cnt, val = heapq.heappop_max(heap)
            res += val
            cnt -= 1

            if prev:
                heapq.heappush_max(heap, prev)
                prev = None

            # Dont push the new cnt to the heap
            if cnt != 0:
                prev = (cnt, val)

        return res
