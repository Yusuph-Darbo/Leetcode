# Approach:
# Use multi-source BFS starting from all treasure cells simultaneously.
# Expand outward level by level, updating each reachable room with its
# shortest distance to a treasure while avoiding walls and revisiting cells.
#
# Time: O(m * n)
# Space: O(m * n)


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        seen = set()

        def addRooms(r, c):
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or (r, c) in seen
                or grid[r][c] == -1
            ):
                return

            seen.add((r, c))
            q.append((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    seen.add((r, c))

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addRooms(r, c + 1)
                addRooms(r, c - 1)
                addRooms(r + 1, c)
                addRooms(r - 1, c)
            dist += 1
