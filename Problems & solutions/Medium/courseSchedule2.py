# Approach:
# Build a prerequisite graph and use DFS to detect cycles. Once a course
# and all its prerequisites are completed, add it to the result. A cycle
# means no valid ordering exists.
#
# Time: O(v + e)
# Space: O(v + e)


class Solution:
    def findOrder(self, numCourses: int, prereq: List[List[int]]) -> List[int]:
        order = []
        graph = defaultdict(list)

        for v, e in prereq:
            graph[v].append(e)

        visiting = set()
        visited = set()

        def dfs(i):
            if i in visiting:
                return False
            if i in visited:
                return True

            visiting.add(i)
            for nei in graph[i]:
                if not dfs(nei):
                    return False

            visiting.remove(i)
            visited.add(i)
            order.append(i)
            return True

        for n in range(numCourses):
            if not dfs(n):
                return []

        return order
