class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, start, end in edges:
            graph[u].append((v, start, end))

        INF = 10**30
        dp = [INF] * n
        dp[0] = 0

        pq = [(0, 0)]  # (time, node)

        while pq:
            t, u = heapq.heappop(pq)
            if t != dp[u]:
                continue
            if u == n - 1:
                return t

            for v, s, e in graph[u]:
                # 현재 시각 t에 u에 있을 때 이 간선을 탈 수 있는지 계산
                if t > e:
                    continue
                depart = max(t, s)
                if depart > e:
                    continue

                nt = depart + 1
                if nt < dp[v]:
                    dp[v] = nt
                    heapq.heappush(pq, (nt, v))

        return -1


# class Solution:
#     def minTime(self, n: int, edges: List[List[int]]) -> int:

#         graph = defaultdict(list)
#         for u, v, start, end in edges:
#             graph[u].append((v, start, end))

#         @cache
#         def dfs(cur, time):
#             # print(cur, time)
#             if cur == n - 1:
#                 return time

#             res = float("inf")
#             for v, start, end in graph[cur]:
#                 if start <= time <= end:
#                     res = min(res, dfs(v, time + 1))
#                 elif time < start:
#                     res = min(res, dfs(cur, start))

#             return res

#         res = dfs(0, 0)
#         return -1 if res == float("inf") else res

