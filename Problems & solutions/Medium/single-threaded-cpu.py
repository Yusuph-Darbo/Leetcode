# Approach:
# Sort tasks by enqueue time and use a min heap to store
# available tasks ordered by processing time and index.
# Simulate the CPU by adding available tasks to the heap
# and always executing the next shortest task.
#
# Time: O(n log n)
# Space: O(n)


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)

        tasks.sort(key=lambda t: t[0])

        res, heap = [], []
        time, i = tasks[0][0], 0

        while heap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1

            if not heap:
                time = tasks[i][0]
            else:
                procTime, index = heapq.heappop(heap)
                time += procTime
                res.append(index)

        return res
