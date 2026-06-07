# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        nodes = dict()
        no_roots = set()

        for parent, child, left in descriptions:
            no_roots.add(child)
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)

            if left: 
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

        root = list(nodes.keys() - no_roots)[0]
        return nodes[root]

