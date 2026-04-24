# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.leaves = [root]

    def insert(self, val: int) -> int:
        
        parent = -1
        for node in self.leaves:
            if node.left is None: 
                node.left = TreeNode(val)
                parent = node.val
                break
            if node.right is None:
                node.right = TreeNode(val)
                parent = node.val
                break
        
        if parent != -1:
            return parent

        new_leaves = []
        for node in self.leaves:
            new_leaves.append(node.left)
            new_leaves.append(node.right)

        self.leaves = new_leaves
        return self.insert(val)

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
