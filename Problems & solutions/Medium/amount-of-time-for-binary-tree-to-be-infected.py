# Approach:
# First, convert the binary tree into an undirected graph by connecting each
# node to its parent and children. Then use BFS starting from the infected
# node, spreading infection to all unvisited neighbors one level at a time.
# The number of BFS levels represents the total time needed.
#
# Time: O(n)
# Space: O(n)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: TreeNode | None, start: int) -> int:
        graph = defaultdict(list)

        def buildGraph(node, parent):
            if not node:
                return

            if parent:
                graph[parent.val].append(node.val)
                graph[node.val].append(parent.val)

            buildGraph(node.left, node)
            buildGraph(node.right, node)

        buildGraph(root, None)

        q = deque([start])
        seen = set()
        time = -1

        while q:
            time += 1
            for _ in range(len(q)):
                node = q.popleft()
                seen.add(node)

                for nei in graph[node]:
                    if nei not in seen:
                        q.append(nei)

        return time
