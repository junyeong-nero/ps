class Node:
    def __init__(
        self,
        val,
        isLeaf,
        topLeft=None,
        topRight=None,
        bottomLeft=None,
        bottomRight=None,
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        
        def dfs(node1, node2):
            
            if node1.isLeaf and node2.isLeaf:
                value = node1.val | node2.val
                return Node(val=value, isLeaf=1)

            elif node1.isLeaf:
                if node1.val == 1:
                    return Node(val=1, isLeaf=1)
                return node2

            elif node2.isLeaf:
                if node2.val == 1:
                    return Node(val=1, isLeaf=1)
                return node1

            d = dict()
            d["topLeft"] = dfs(node1.topLeft, node2.topLeft)
            d["topRight"] = dfs(node1.topRight, node2.topRight)
            d["bottomLeft"] = dfs(node1.bottomLeft, node2.bottomLeft)
            d["bottomRight"] = dfs(node1.bottomRight, node2.bottomRight)

            check = all([(node.val == 1 and node.isLeaf == 1) for node in d.values()])
            if check:
                return Node(val=1, isLeaf=1)

            return Node(
                val=1, 
                isLeaf=0, 
                **d
            )

        return dfs(quadTree1, quadTree2)        

    
