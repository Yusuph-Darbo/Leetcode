# Approach:
# Use breadth-first search to traverse the tree level by level.
# Track the last node processed at each level, since it represents
# the node visible from the right side of the tree.
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            r = None

            for _ in range(qLen):
                node = q.popleft()
                if node:
                    r = node
                    q.append(node.left)
                    q.append(node.right)

            if r:
                res.append(r.val)

        return res
