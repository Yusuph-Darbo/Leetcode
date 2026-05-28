# Approach:
# Use preorder traversal to determine the root node order
# and a hash map to quickly find each root's position in
# the inorder traversal. Recursively build the left and
# right subtrees using the inorder boundaries.
#
# Time: O(n)
# Space: O(n)


#  Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {}

        for val, index in enumerate(inorder):
            indices[index] = val

        self.pre = 0

        def dfs(l, r):
            if l > r:
                return None

            rootVal = preorder[self.pre]
            self.pre += 1
            root = TreeNode(rootVal)
            mid = indices[rootVal]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root

        return dfs(0, len(inorder) - 1)
