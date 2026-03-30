def solution(depth, money, excavate):
    n = len(depth)
    
    # dp[l][r]: l~r 구간에서 보물을 확실히 찾는 최소 비용
    dp = [[0] * n for _ in range(n)]
    pick = [[-1] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = depth[i]
        pick[i][i] = i
    
    for length in range(2, n + 1):
        for l in range(n - length + 1):
            r = l + length - 1
            best_cost = float('inf')
            best_k = -1
            
            for k in range(l, r + 1):
                left_cost = dp[l][k - 1] if k > l else 0
                right_cost = dp[k + 1][r] if k < r else 0
                cost = depth[k] + max(left_cost, right_cost)
                
                if cost < best_cost:
                    best_cost = cost
                    best_k = k
            
            dp[l][r] = best_cost
            pick[l][r] = best_k
    
    # 문제 조건상, 최소 보장 비용 <= money 가 보장됨
    l, r = 0, n - 1
    
    while l <= r:
        k = pick[l][r]
        res = excavate(k + 1)  # 1-indexed
        
        if res == 0:
            return k + 1
        elif res == -1:
            r = k - 1
        else:  # res == 1
            l = k + 1

    return -1
