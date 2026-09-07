# Approach:
# Use breadth-first traversal to visit each node in the tree.
# Swap the left and right children of every node.
# Continue until all nodes have been processed.
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None

        queue = [root]

        while queue:
            curr = queue.pop(0)

            curr.left, curr.right = curr.right, curr.left

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        return root
