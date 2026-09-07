# Approach:
# Use a stack with a visited flag to simulate recursive postorder traversal.
# Push nodes back onto the stack as visited before processing their children.
# Process the node only after its left and right subtrees have been handled.
# This visits nodes in left-right-root order.
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        visit = [False]
        res = []

        while stack:
            curr = stack.pop()
            v = visit.pop()

            if curr:
                if v:
                    res.append(curr.val)

                else:
                    stack.append(curr)
                    visit.append(True)
                    stack.append(curr.right)
                    visit.append(False)
                    stack.append(curr.left)
                    visit.append(False)

        return res
