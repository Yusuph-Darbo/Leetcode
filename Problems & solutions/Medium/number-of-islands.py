# Approach:
# Traverse the grid and start a DFS whenever an unvisited land cell is
# found. During the DFS, mark all connected land cells as visited. Each
# DFS traversal represents one distinct island.
#
# Time: O(m * n)
# Space: O(m * n)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        island = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    island += 1

        return island
