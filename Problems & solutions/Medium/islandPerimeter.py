# Approach:
# Use BFS to traverse all land cells in the island. For each cell, examine
# its four neighbors; if a neighbor is out of bounds or water, it contributes
# one edge to the perimeter. Sum these contributions across the entire island.
#
# Time: O(m * n)
# Space: O(m * n)


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(r, c):
            q = deque([(r, c)])
            visited.add((r, c))
            perimeter = 0

            while q:
                x, y = q.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if (
                        nx < 0
                        or ny < 0
                        or nx >= rows
                        or ny >= cols
                        or grid[nx][ny] == 0
                    ):
                        perimeter += 1
                    elif (nx, ny) not in visited:
                        visited.add((nx, ny))
                        q.append((nx, ny))

            return perimeter

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return bfs(r, c)

        return 0
