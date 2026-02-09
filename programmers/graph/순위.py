from collections import defaultdict, deque

def solution(n, results):
    
    in_graph = defaultdict(list)
    out_graph = defaultdict(list)
    for a, b in results:
        in_graph[a].append(b)
        out_graph[b].append(a)
    
    def query(root):
        winners = set()
        losers = set()
        
        q = deque([root])
        while q:
            tar = q.popleft()
            winners.add(tar)
            for node in out_graph[tar]:
                if node in winners:
                    continue
                q.append(node)
        
        q = deque([root])
        while q:
            tar = q.popleft()
            losers.add(tar)
            for node in in_graph[tar]:
                if node in losers:
                    continue
                q.append(node)
        
        if len(winners | losers) == n:
            return True
        return False
                    
    answer = [1 if query(node) else 0 for node in range(1, n + 1)]
    answer = sum(answer)
    return answer
