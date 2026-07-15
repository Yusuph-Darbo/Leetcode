# Approach:
# Build an adjacency list for the graph, then use DFS to explore all
# reachable nodes starting from the source. If the destination is found
# during traversal, return True; otherwise, return False.
#
# Time: O(n + e)
# Space: O(n + e)


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, dest: int) -> bool:
        graph = collections.defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        stack = [source]
        visited = set()

        while stack:
            node = stack.pop()

            if node == dest:
                return True

            if node in visited:
                continue

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

        return False
