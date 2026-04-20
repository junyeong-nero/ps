from collections import defaultdict, deque, Counter


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # no cycles
        # select vertices to break cycles
        # remove edge first -> check the graph requires tree.

        n = len(edges)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def is_tree(node, ignore=(-1, -1)):

            q = deque([node])
            visited = Counter()

            while q:

                cur = q.popleft()
                if visited[cur] == 1:
                    return False
                visited[cur] += 1

                for node in graph[cur]:
                    if (node, cur) == ignore or (cur, node) == ignore:
                        continue
                    if visited[node] == 1:
                        continue
                    q.append(node)

            # print(counter)
            return True

        for u, v in edges[::-1]:
            if is_tree(u, (u, v)):
                return [u, v]

        return []


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parents = [i for i in range(N + 1)]
        rank = [1] * (N + 1)

        def find(i):
            if parents[i] != i:
                parents[i] = find(parents[i])
            return parents[i]

        def union(a, b):
            parentA = find(a)
            parentB = find(b)

            if parentA == parentB:
                return False

            if rank[parentA] > rank[parentB]:
                parents[parentB] = parentA
                rank[parentA] += rank[parentB]
            else:
                parents[parentA] = parentB
                rank[parentB] += rank[parentA]
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]
