# Approach:
# Build an adjacency list from the pairs. The two endpoints of the array have
# only one neighbor, so start DFS from either endpoint and avoid revisiting the
# previous node.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def restoreArray(self, pairs: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        root = None
        array = []

        for v, e in pairs:
            graph[v].append(e)
            graph[e].append(v)

        for node, nei in graph.items():
            if len(nei) == 1:
                root = node
                break

        def dfs(node, prev):
            array.append(node)
            for nei in graph[node]:
                if nei != prev:
                    dfs(nei, node)

        dfs(root, None)

        return array
