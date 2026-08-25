# Approach:
# Use BFS from all border 'O's and mark them as safe. Then flip all
# remaining 'O's to 'X' and restore the safe cells back to 'O'.
#
# Time: O(m * n)
# Space: O(m * n)


class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(r, c):
            if grid[r][c] != "O":
                return

            grid[r][c] = "T"
            q = deque([(r, c)])

            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "O":
                        q.append((nx, ny))
                        grid[nx][ny] = "T"

        for r in range(rows):
            bfs(r, 0)
            bfs(r, cols - 1)

        for c in range(cols):
            bfs(0, c)
            bfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "O":
                    grid[r][c] = "X"
                if grid[r][c] == "T":
                    grid[r][c] = "O"
