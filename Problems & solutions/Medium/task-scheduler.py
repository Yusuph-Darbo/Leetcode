# Approach:
# Count the frequency of each task and store the counts in a max heap.
# Repeatedly execute the most frequent available task while using a queue
# to track tasks that are in their cooldown period. Continue until all
# tasks have been completed.
#
# Time: O(n log k)
# Space: O(k)
# where k is the number of distinct tasks.


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [cnt for cnt in count.values()]

        heapq.heapify_max(heap)

        time = 0
        q = collections.deque()

        while heap or q:
            time += 1
            if heap:
                cnt = heapq.heappop_max(heap)
                cnt -= 1
                if cnt > 0:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush_max(heap, q.popleft()[0])

        return time
