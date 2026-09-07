# Approach:
# Traverse the grid and perform BFS whenever an unvisited land cell is found.
# During the traversal, count the number of connected land cells to determine
# the island's area, and keep track of the maximum area encountered.
#
# Time: O(m * n)
# Space: O(m * n)


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seen = set()
        res = 0

        def bfs(r, c):
            q = deque([(r, c)])
            seen.add((r, c))
            size = 1

            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = dx + x, dy + y

                    if (
                        nx < 0
                        or ny < 0
                        or nx >= rows
                        or ny >= cols
                        or grid[nx][ny] == 0
                    ):
                        continue
                    elif (nx, ny) not in seen:
                        q.append((nx, ny))
                        seen.add((nx, ny))
                        size += 1

            return size

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, bfs(r, c))

        return res
