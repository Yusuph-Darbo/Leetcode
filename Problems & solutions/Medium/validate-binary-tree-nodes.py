# Approach:
# Track which nodes already have a parent to identify the root. Then use DFS
# to detect cycles/duplicate visits and finally check that every node was visited.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        hasParents = set(leftChild + rightChild)

        hasParents.discard(-1)

        if len(hasParents) == n:
            return False

        root = -1
        for i in range(n):
            if i not in hasParents:
                root = i

        seen = set()

        def dfs(i):
            if i in seen:
                return False
            if i == -1:
                return True

            seen.add(i)

            return dfs(leftChild[i]) and dfs(rightChild[i])

        return dfs(root) and len(seen) == n
