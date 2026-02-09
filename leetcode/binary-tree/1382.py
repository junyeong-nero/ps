# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        values = []
        q = deque([root])
        while q:
            tar = q.popleft()
            values.append(tar.val)
            if tar.left: q.append(tar.left)
            if tar.right: q.append(tar.right)

        values = sorted(values)
        # print(values)

        def generate(arr):
            n = len(arr)
            if n == 0:
                return None
            if n == 1:
                return TreeNode(val=arr[0])
            
            index = n // 2
            node = TreeNode(val=arr[index])
            node.left = generate(arr[:index])
            node.right = generate(arr[index + 1:])
            return node
            
        res = generate(values)
        return res
