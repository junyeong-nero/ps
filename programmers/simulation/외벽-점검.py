from itertools import permutations

def solution(n, weak, dist):
    m = len(weak)
    extended = weak + [w + n for w in weak]
    answer = len(dist) + 1

    for start in range(m):
        for friends in permutations(dist):
            count = 1
            limit = extended[start] + friends[count - 1]

            for idx in range(start, start + m):
                if extended[idx] > limit:
                    count += 1
                    if count > len(dist):
                        break
                    limit = extended[idx] + friends[count - 1]

            answer = min(answer, count)

    return answer if answer <= len(dist) else -1

# import heapq

# class DSU:
    
#     def __init__(self, n):
#         self.parent = list(range(n))
        
#     def find(self, x):
#         if x != self.parent[x]:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]
    
#     def union(self, x, y):
#         parentx, parenty = self.find(x), self.find(y)
#         if parentx < parenty:
#             self.parent[parenty] = parentx
#         else:
#             self.parent[parentx] = parenty
        

# def solution(n, weak, dist):
    
#     # circular boundary 문제.
#     # 1, 5, 6, 10 -> 인데 사실은 10, 1 -> 거리가 3 이라고 고려해야 함.
#     # dist 기준으로 묶어야 할 듯.
    
#     # 어떤 포인트를 점검해야 한다고 생각해보자.
#     # 만약 왼쪽 포인트의 거리와 오른쪽 포인트까지 거리를 계산하고
#     # 짧은 쪽 포인트와 합치면 greedy 하게 문제를 풀 수 있을가?
#     # 거리가 짧은 녀석끼리 합치는 방식으로 해야할듯
#     # union & find ?
    
#     # 일단 max 보다 길이가 긴 녀석들은 날려야 됨.
#     # 짧은 애들끼리 합침. 다 합쳤을 떄...? 커버가 안되면 끝?

    
#     m = len(weak)
#     d = DSU(m)
    
#     q = []
#     for i in range(m - 1):
#         temp = weak[i + 1] - weak[i]
#         heapq.heappush(q, (temp, i + 1, i))
        
#     heapq.heappush(q, (weak[0] + n - weak[-1], 0, m - 1))
#     merged = [False] * m
    
    
#     while q:
#         cur_dist, a, b = heapq.heappop(q)
#         if merged[a] and merged[b]:
#             continue
            
#         d.union(a, b)
#         print(cur_dist, a, b)
#         merged[a] = True
#         merged[b] = True
    
#     print(d.parent)
    
#     answer = 0
#     return answer
