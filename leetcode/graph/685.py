class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        # directed graph
        n = len(edges)

        indegree = [0] * (n + 1)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        def check(root, ignored=(-1, -1)):

            q = deque([root])
            visited = set()

            while q:
                
                cur = q.popleft()
                visited.add(cur)

                for node in graph[cur]:
                    if (cur, node) == ignored:
                        continue
                    if node in visited:
                        return False

                    q.append(node)

            return len(visited) == n

        roots = [node for node in range(1, n + 1) if indegree[node] == 0]

        for u, v in edges[::-1]:
            # remove u, v edge
            indegree[v] -= 1

            if indegree[v] == 0 and check(v, (u, v)):
                return [u, v]

            if indegree[u] == 0 and check(u, (u, v)):
                return [u, v]

            for root in roots:
                if check(root, (u, v)):
                    return [u, v]

            indegree[v] += 1

        return []
