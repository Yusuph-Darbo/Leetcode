# Approach:
# Perform a level-order traversal (BFS) of the tree. For each level, track
# the maximum node value encountered and add it to the result list.
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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            qLen = len(q)
            val = float("-inf")

            for _ in range(qLen):
                node = q.popleft()
                val = max(val, node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(val)

        return res
