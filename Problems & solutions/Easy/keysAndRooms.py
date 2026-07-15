# Approach:
# Use DFS starting from room 0 and follow the keys found in each room to
# visit additional rooms. After the traversal, check whether every room
# has been visited.
#
# Time: O(n + k)
# Space: O(n)


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set()

        def dfs(i):
            seen.add(i)
            for neighbor in rooms[i]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        dfs(0)

        return len(seen) == len(rooms)
