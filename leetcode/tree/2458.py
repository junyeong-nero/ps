class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        # 각 노드의 높이 (아래 방향)
        height = {}

        def get_height(node):
            if not node:
                return 0
            height[node.val] = 1 + max(get_height(node.left), get_height(node.right))
            return height[node.val]

        get_height(root)

        # remain[v] = 노드 v를 제거했을 때 트리의 최대 높이
        remain = {}

        def dfs(node, depth, max_without):
            """
            node     : 현재 노드
            depth    : 현재 노드의 깊이 (루트=0)
            max_without : 현재 노드를 제거했을 때 보장되는 높이
                          (조상 라인에서 형제들이 커버하는 최대값)
            """
            if not node:
                return

            remain[node.val] = max_without

            left_h = height.get(node.left.val, 0) if node.left else 0
            right_h = height.get(node.right.val, 0) if node.right else 0

            # 왼쪽 자식을 지우면 → 오른쪽이 살아있고, 현재 depth까지는 보장
            dfs(node.left, depth + 1, max(max_without, depth + right_h))
            # 오른쪽 자식을 지우면 → 왼쪽이 살아있고, 현재 depth까지는 보장
            dfs(node.right, depth + 1, max(max_without, depth + left_h))

        dfs(root, 0, 0)

        return [remain[q] for q in queries]

        ### BFS approach

        nodes = [None] * (n + 1)
        nodes_level = [0] * (n + 1)

        q = deque([root])
        level = 0

        while q:

            for _ in range(len(q)):

                cur = q.popleft()
                nodes[cur.val] = cur
                nodes_level[cur.val] = level

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            level += 1

        # print(n)
        # print(nodes)
        # print(nodes_level)

        def func(remove_node):
            new_levels = nodes_level[:]
            q = deque([remove_node])
            while q:

                cur = q.popleft()
                new_levels[cur.val] = 0

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            return max(new_levels)

        res = []
        for query in queries:
            res.append(func(nodes[query]))

        return res

