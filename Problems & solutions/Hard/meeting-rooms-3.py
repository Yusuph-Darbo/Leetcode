# Approach:
# Sort meetings by start time. Use a min-heap of available room numbers and
# another min-heap of (end_time, room_number) for occupied rooms.
# Free rooms whose meetings have ended, assign the smallest available room,
# or delay the meeting until the earliest room becomes free.
#
# Time: O(m log m + m log n)
# Space: O(n)


class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        available = [i for i in range(n)]
        used = []
        count = [0] * n

        for start, end in meetings:
            while used and used[0][0] <= start:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)

            if not available:
                end_time, room = heapq.heappop(used)
                end = end_time + (end - start)
                heapq.heappush(available, room)

            room = heapq.heappop(available)
            heapq.heappush(used, (end, room))
            count[room] += 1

        return count.index(max(count))
