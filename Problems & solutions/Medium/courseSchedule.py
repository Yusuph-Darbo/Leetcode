# Approach:
# Build a graph of course prerequisites and use DFS to detect cycles.
# Track courses currently being visited; finding one again means a cycle
# exists. Once a course is fully checked, mark it as having no prerequisites.
#
# Time: O(V + E)
# Space: O(V + E)


class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:
        preMap = defaultdict(list)

        for crs, pre in prereq:
            preMap[crs].append(pre)

        seen = set()

        def dfs(crs):
            # Cycle
            if crs in seen:
                return False

            if preMap[crs] == []:
                return True

            seen.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            seen.remove(crs)
            preMap[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
