# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        q = deque([(root, 0)])
        res = 0

        while q:
            tar, value = q.popleft()
            new_value = (value << 1) | tar.val
            if not tar.left and not tar.right:
                # leafnode
                res += new_value
            
            if tar.left: q.append((tar.left, new_value))
            if tar.right: q.append((tar.right, new_value))

        return res
            
