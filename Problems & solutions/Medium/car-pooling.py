# Approach:
# Sort trips by pickup location and use a min heap to track
# active trips by their drop-off locations. Remove passengers
# whose trips have ended before each pickup, then check whether
# adding the new passengers exceeds the vehicle's capacity.
#
# Time: O(n log n)
# Space: O(n)


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])

        heap = []
        cap = 0

        for numPass, start, end in trips:
            while heap and heap[0][0] <= start:
                cap -= heapq.heappop(heap)[1]

            cap += numPass

            if cap > capacity:
                return False

            heapq.heappush(heap, (end, numPass))

        return True
