import heapq
from collections import defaultdict

def solution(alp, cop, problems):
    
    target_alp = max(alp_req for alp_req, _, _, _, _ in problems)
    target_cop = max(cop_req for _, cop_req, _, _, _ in problems)
    print(target_alp, target_cop)
    
    n = len(problems)
    # 최단시간? => 이거 dijkstra 임;
    
    # dist[a][b] : alp = a, cor = b 까지 도달하는데 걸리는 최소 시간
    dist = defaultdict(dict)
    dist[alp][cop] = 0
    
    def get_dist(a, c):
        if a in dist and c in dist[a]:
            return dist[a][c]
        return float("inf")
    
    q = [(0, alp, cop)]    
    while q:
        
        cur_dist, cur_alp, cur_cop = heapq.heappop(q)
        if cur_alp >= target_alp and cur_cop >= target_cop:
            break
        
        for i in range(n):
            if cur_alp >= problems[i][0] and cur_cop >= problems[i][1]:
                next_alp = min(cur_alp + problems[i][2], target_alp)
                next_cop = min(cur_cop + problems[i][3], target_cop)
                next_dist = cur_dist + problems[i][4]
            
            else:
                next_alp = max(cur_alp, problems[i][0])
                next_cop = max(cur_cop, problems[i][1])
                next_dist = cur_dist + max(0, problems[i][0] - cur_alp) + max(0, problems[i][1] - cur_cop)
                
            if next_dist < get_dist(next_alp, next_cop):
                dist[next_alp][next_cop] = next_dist
                heapq.heappush(q, (next_dist, next_alp, next_cop))
                    
                    
    res = dist[target_alp][target_cop]
    return res
