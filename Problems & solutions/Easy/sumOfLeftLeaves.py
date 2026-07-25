# Approach:
# Use DFS to traverse the tree while tracking whether each node is a left
# child. When a leaf node is reached, add its value to the sum only if it
# is a left leaf.
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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left):
            if not node:
                return 0

            if not node.left and not node.right:
                if is_left:
                    return node.val
                else:
                    return 0

            leftVal = dfs(node.left, True)
            rightVal = dfs(node.right, False)

            return leftVal + rightVal

        return dfs(root, False)
