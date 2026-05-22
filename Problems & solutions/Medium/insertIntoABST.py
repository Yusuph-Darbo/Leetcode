# Approach:
# Traverse the BST iteratively to find the correct position
# for the new value based on BST ordering rules.
# Insert the new node when an empty left or right child is found.
#
# Time: O(h)
# Space: O(1)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val)

        curr = root
        while True:
            if val > curr.val:
                if curr.right == None:
                    curr.right = TreeNode(val)
                    return root
                curr = curr.right

            else:
                if curr.left == None:
                    curr.left = TreeNode(val)
                    return root
                curr = curr.left
