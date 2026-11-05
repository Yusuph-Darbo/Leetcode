# Approach:
# First, use DFS to identify and label every connected island with a unique ID,
# storing each island's area. Then, try flipping every zero to one and calculate
# the resulting area by adding the sizes of its distinct neighboring islands.
# Use a set to avoid counting the same island more than once.
#
# Time: O(n^2)
# Space: O(n^2)


class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        areas = [0, 0]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for r in range(n):
            for c in range(n):
                if grid[r][c] != 1:
                    continue

                label = len(areas)
                stack = [(r, c)]
                grid[r][c] = label
                area = 0

                while stack:
                    x, y = stack.pop()
                    area += 1

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                            grid[nx][ny] = label
                            stack.append((nx, ny))

                areas.append(area)

        answer = max(areas)

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    labels = set()

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if 0 <= nr < n and 0 <= nc < n:
                            if grid[nr][nc] > 1:
                                labels.add(grid[nr][nc])

                    area = 1 + sum(areas[label] for label in labels)
                    answer = max(answer, area)

        return answer
