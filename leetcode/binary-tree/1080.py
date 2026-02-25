# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        
        def dfs(cur, value):
            if not cur.left and not cur.right:
                return value + cur.val >= limit

            left = dfs(cur.left, value + cur.val) if cur.left else False
            right = dfs(cur.right, value + cur.val) if cur.right else False
            if not left:
                cur.left = None
            if not right:
                cur.right = None

            return left or right
                
        temp = dfs(root, 0)
        if not temp:
            return None

        return root
