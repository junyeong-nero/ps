# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        if (not root1 and not root2): return True
        if (not root1 and root2): return False
        if (root1 and not root2): return False

        if (root1.val != root2.val):
            return False

        # FLIP
        L = self.flipEquiv(root1.left, root2.right)
        R = self.flipEquiv(root1.right, root2.left)
        if L and R:
            return True

        # NO-FLIP
        L = self.flipEquiv(root1.left, root2.left)
        R = self.flipEquiv(root1.right, root2.right)
        if L and R:
            return True

        return False

        
