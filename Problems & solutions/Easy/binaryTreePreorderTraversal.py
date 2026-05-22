# Approach:
# Use a stack to perform iterative inorder traversal.
# Traverse left as far as possible, pushing nodes onto the stack.
# Process the node, then move to its right subtree.
# This visits nodes in left-root-right order.
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        stack = [root]
        res = []

        while len(stack) > 0:
            curr = stack.pop()
            res.append(curr.val)

            if curr.right:
                stack.append(curr.right)

            if curr.left:
                stack.append(curr.left)

        return res
