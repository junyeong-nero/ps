class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:

        MOD = 10 ** 9 + 7

        graph = defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w
        
        def func(node):
            
            q = [(0, node)]
            dist = dict()
            dist[node] = 0

            while q:
                d, cur = heappop(q)
                for node, weight in graph[cur].items():
                    if d + weight < dist.get(node, float("inf")):
                        dist[node] = d + weight
                        heappush(q, (d + weight, node))
            
            return dist
    
        dst = func(n)

        dag = defaultdict(dict)
        for u, v, w in edges:
            if dst[u] < dst[v]: dag[u][v] = w
            if dst[v] < dst[u]: dag[v][u] = w

        @cache
        def dfs(cur):
            if cur == 1:
                return 1
            return sum(dfs(node) for node in dag[cur]) % MOD
            
        res = dfs(n)
        return res


