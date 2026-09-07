# Approach:
# Use multi-source BFS by starting from all initially rotten oranges.
# At each minute, rot all adjacent fresh oranges and track the remaining
# number of fresh oranges. Return the time required to rot all oranges, or
# -1 if some fresh oranges cannot be reached.
#
# Time: O(m * n)
# Space: O(m * n)


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        fresh = 0
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        while fresh > 0 and q:
            qLen = len(q)

            for i in range(qLen):
                x, y = q.popleft()

                for dx, dy in direction:
                    nx, ny = dx + x, dy + y

                    if nx in range(rows) and ny in range(cols) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        q.append((nx, ny))
                        fresh -= 1
            time += 1

        if fresh == 0:
            return time
        else:
            return -1
