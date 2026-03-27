class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges) + 1

        # n 10^5 -> O(N log N)
        # graph traverse in log N

        # mark node i
        # adj node is even => time + 2
        # adj node is odd  => time + 1
        # max time

        # node i -> j
        # if node i is even => 
        # 

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)


        leaves = [node for node in graph if len(graph[node]) == 1]
        print(leaves)

        ### Leafnode -> heapify
        res = [0] * n

        # DFS

        @cache
        def func(cur, prev=-1, time=0):

            res[cur] = max(res[cur], time)
            time += 1 if cur & 1 == 1 else 2
            for node in graph[cur]:
                if node == prev: continue
                func(node, cur, time)

        for leaf in leaves:
            func(leaf)

        print(res)
        return res



        ### BFS approach

        hist = dict()

        @cache
        def func(cur, prev=-1):
            res = dict()
            for node in graph[cur]:
                if node == prev: continue
                if node & 1 == 0:
                    res[node] = 2 + func(node, cur)
                if node & 1 == 1:
                    res[node] = 1 + func(node, cur)

            hist[cur] = res
            return max(res.values()) if res else 0


        # O(n^2)
        res = []
        for i in range(n):
            temp = func(i)
            res.append(temp)

        return res


class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        down = [0] * n   # u에서 아래로만 갔을 때 최대 시간
        up = [0] * n     # u에서 위/바깥으로 갔을 때 최대 시간
        parent = [-1] * n

        def cost(to_node: int) -> int:
            return 1 if to_node & 1 else 2

        # 1) down 계산
        def dfs1(u: int, p: int) -> None:
            parent[u] = p
            best = 0
            for v in graph[u]:
                if v == p:
                    continue
                dfs1(v, u)
                best = max(best, cost(v) + down[v])
            down[u] = best

        # 2) up 계산 (rerooting)
        def dfs2(u: int, p: int) -> None:
            # u의 각 자식 방향 candidate = cost(v) + down[v]
            best1 = best2 = 0
            best1_child = -1

            for v in graph[u]:
                if v == p:
                    continue
                val = cost(v) + down[v]
                if val > best1:
                    best2 = best1
                    best1 = val
                    best1_child = v
                elif val > best2:
                    best2 = val

            for v in graph[u]:
                if v == p:
                    continue

                # u에서 v 말고 다른 방향으로 갈 때의 최대값
                use = best2 if best1_child == v else best1

                # v 입장에서 부모 u 쪽으로 한 칸 올라가는 비용은 cost(u)
                # u에서 바깥으로 가는 최선:
                #   1) u의 위쪽(up[u])
                #   2) u의 다른 자식 방향(use)
                up[v] = cost(u) + max(up[u], use)

                dfs2(v, u)

        dfs1(0, -1)
        dfs2(0, -1)

        ans = [0] * n
        for i in range(n):
            ans[i] = max(down[i], up[i])

        return ans
