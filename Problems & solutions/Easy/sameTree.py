# Approach:
# Use iterative inorder traversal on both trees simultaneously.
# Compare corresponding nodes for structure and value equality.
# If any mismatch is found, return False; otherwise both trees are identical.
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        s1 = []
        s2 = []
        curr1 = p
        curr2 = q

        while s1 or s2 or curr1 or curr2:
            if (curr1 is None) != (curr2 is None):
                return False

            while curr1 and curr2:
                s1.append(curr1)
                s2.append(curr2)

                curr1 = curr1.left
                curr2 = curr2.left

                if type(curr1) != type(curr2):
                    return False
                if curr1 is None:
                    continue
                if curr1.val != curr2.val:
                    return False

            if len(s1) != len(s2):
                return False
            if not s1 and not s2:
                break
            curr1 = s1.pop()
            curr2 = s2.pop()

            if curr1.val != curr2.val:
                return False

            curr1 = curr1.right
            curr2 = curr2.right

        return True
