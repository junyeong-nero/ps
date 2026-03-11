class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # DAG
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)

        res = [[] for _ in range(n)]

        # dfs or bfs?
        def func(root):

            q = deque([root])
            visited = set()

            while q:

                tar = q.popleft()
                if tar not in visited and tar != root:
                    res[tar].append(root)
                visited.add(tar)

                for node in graph[tar]:
                    if node in visited:
                        continue
                    q.append(node)

        
        for i in range(n):
            func(i)

        return res
